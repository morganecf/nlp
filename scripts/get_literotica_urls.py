"""
Save literotica urls to file so that these can be downloaded.
"""

import os
import requests
import argparse
from bs4 import BeautifulSoup

def get_soup(url):
  response = requests.get(url)
  return BeautifulSoup(response.text, 'html.parser')

def filter_urls(url, fn):
  soup = get_soup(url)
  urls = soup.find_all('a')
  return [url.get('href') for url in urls if fn(url.get('href'))]

def is_category_url(url):
  return '/c/' in url

def is_story_url(url):
  return url.startswith('https://www.literotica.com/s/')

def is_category_page_url(url):
  return url.endswith('-page')

parser = argparse.ArgumentParser()
parser.add_argument('--urls', required=True, type=str, help='path to save urls (ex: urls.tsv)')
parser.add_argument('--category', type=str, help='start with this category (ex: mind-control)', default=None)

args = parser.parse_args()

if os.path.isfile(args.urls):
  fp = open(args.urls, 'a')
else:
  fp = open(args.urls, 'w')
  fp.write('story_url\tnum_pages\tcategory\tauthor\tnum_comments\tnum_views\tnum_favorites\n')

base_url = 'https://www.literotica.com/stories/'
category_urls = filter_urls(base_url, is_category_url)
categories = [url.split('/')[-1] for url in category_urls]

start_index = 0 if args.category is None else categories.index(args.category)

print('Starting with category:', args.category, start_index)

for category, category_url in list(zip(categories, category_urls))[start_index:]:
  print('category:', category)
  story_urls = filter_urls(category_url, is_story_url)
  page_urls = filter_urls(category_url, is_category_page_url)
  print('\t', len(story_urls), 'stories on first page', len(page_urls), 'more pages')

  for page_url in page_urls:
    story_urls.extend(filter_urls(page_url, is_story_url))

  print('\ttotal story urls for this category:', len(story_urls))

  for story_url in story_urls:
    soup = get_soup(story_url)

    try:
      pages_caption = soup.find('span', class_='b-pager-caption-t').text
      num_pages = pages_caption.split()[0]
    except:
      num_pages = '1'

    author = soup.find('span', class_='b-story-user-y').find('a').text.strip()

    try:
      stats = soup.find('span', class_='b-story-stats').text
      num_comments, num_views, num_favorites = [n for i, n in enumerate(stats.split()) if i % 2 == 0]
    except:
      num_comments, num_views, num_favorites = 'None', 'None', 'None'

    data = '\t'.join([story_url, num_pages, category, author, num_comments, num_views, num_favorites])
    print('\t', data)
    fp.write(data + '\n')

fp.close()
