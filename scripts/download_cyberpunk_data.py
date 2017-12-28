"""
Save Archive Of Our Own cyberpunk story urls with some metadata.

To scrape urls:
  python download_cyberpunk_data.py --urls urls.tsv

To download data (will scrape urls first if urls.tsv is empty):
  python download_cyberpunk_data.py --urls urls.tsv --data_dir data/cyberpunk_data/
"""

import os
import json
import string
import argparse
import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://archiveofourown.org/works/'
BASE_CYBERPUNK_URL = 'https://archiveofourown.org/tags/Cyberpunk/works'

'''
NOTE: might need to do something about CW (need to hit button)
'''

def format_title(title):
  for p in string.punctuation:
    title = title.replace(p, '')
  return '-'.join(title.lower().split()) + '.json'

def to_str(el):
  s = el.text.strip()
  if type(s) is bytes:
    return s.decode('utf-8')
  return s

def get_tags(soup, tag):
  tags = soup.find('dd', class_=tag)
  if tags:
    return [to_str(li) for li in tags.find_all('li')]
  return []

def get_stat(soup, stat):
  try:
    return to_str(soup.find('dd', class_=stat))
  except:
    return None

def get_attr(soup, el, class_):
  try:
    return to_str(soup.find(el, class_=class_))
  except:
    return None

def get_story_data(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.text)

  data = {
    'ratings': get_tags(soup, 'rating'),
    'warnings': get_tags(soup, 'warning'),
    'fandoms': get_tags(soup, 'fandom'),
    'relationships': get_tags(soup, 'relationship'),
    'characters': get_tags(soup, 'character'),
    'published': get_stat(soup, 'published'),
    'status': get_stat(soup, 'status'),
    'words': get_stat(soup, 'words'),
    'chapters': get_stat(soup, 'chapters'),
    'comments': get_stat(soup, 'comments'),
    'kudos': get_stat(soup, 'kudos'),
    'hits': get_stat(soup, 'hits'),
    'title': get_attr(soup, 'h2', 'title'),
    'author': get_attr(soup, 'h3', 'byline'),
    'summary': get_attr(soup, 'div', 'summary'),
    'notes': get_attr(soup, 'div', 'notes')
  }

  story_container = soup.find('div', id='chapters')
  paragraphs = [to_str(p) for p in story_container.find_all('p')]

  data['paragraphs'] = paragraphs

  return data

def download_stories(urls, data_dir):
  for i, url in enumerate(urls):
    print('url:', url, '\t', i, '/', len(urls))
    story_data = get_story_data(url)
    title = format_title(story_data['title'])
    path = os.path.join(data_dir, title)
    json.dump(dict(story_data), open(path, 'w'), indent=4)

def save_urls(urls_file, num_pages, data_dir=None):
  for i in range(1, num_pages + 1):
    print('Fetching urls on page', i)
    url = BASE_CYBERPUNK_URL + '?page=' + str(i)
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    hrefs = [a.get('href') for a in soup.find_all('a') if a.get('href').startswith('/works/')]
    num_stories = 0
    for href in hrefs:
      try:
        story_id = int(href.split('/')[2])
        story_url = BASE_URL + str(story_id) + '?view_full_work=true'
        urls_file.write(story_url + '\n')
        num_stories += 1
      except:
        pass
    print('\t', num_stories, 'stories')
  urls_file.close()

def save_and_download(url_path, data_dir):
  save_urls(url_path)
  urls = open(url_path).read().splitlines()
  download_stories(urls, data_dir)


parser = argparse.ArgumentParser()
parser.add_argument('--urls', required=True, type=str, help='path to save urls (ex: urls.tsv)')
parser.add_argument('--data_dir', type=str, help='path to directory where story data will be downloaded', default=None)
parser.add_argument('--pages', type=int, help='number of pages to get', default=33)

args = parser.parse_args()

if args.data_dir:
  if os.path.isfile(args.urls):
    urls = open(args.urls).read().splitlines()
    if len(urls) > 0:
      download_stories(urls, args.data_dir)
    else:
      save_and_download(args.urls, args.data_dir, args.pages)
  else:
    save_and_download(args.urls, args.data_dir, args.pages)
else:
  save_urls(args.urls, args.pages)
