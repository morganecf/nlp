"""
Creates dataset of stories available as of 12/24/2017.

urls is a tsv with format:
  story_url, num_pages, author, category, num_comments, num_views, num_favorites
"""

import os
import sys
import json
import requests
import argparse
import pandas as pd
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument('--urls', required=True, type=str, help='urls to scrape, generated from download_literotica_data.py')
parser.add_argument('--data_dir', required=True, type=str, help='directory in which to save output jsons')
parser.add_argument('--sample', type=float, default=1, help='fraction of stories to sample per category (1 to get all stories)')

args = parser.parse_args()

urls = pd.read_csv(args.urls, sep='\t')
urls = urls.drop_duplicates('story_url')

by_category = urls.groupby('category')

for category, group in by_category:
  sample = group.sample(frac=args.sample)
  num_stories = len(sample.story_url)

  print('Category:', category)

  out = open(os.path.join(args.data_dir, category + '.txt'), 'w')

  i = 1
  for index, row in sample.iterrows():
    url = row['story_url']
    num_pages = int(row['num_pages'])
    pages = [url + '?page=' + str(i) for i in range(2, num_pages + 1)]

    print('\t', url, num_pages, 'pages\t', i, '/', num_stories)

    story = ''
    for page in pages:
      response = requests.get(page)
      soup = BeautifulSoup(response.text)
      text = soup.find('div', class_='b-story-body-x').text
      story += text + '\n\n'

    row_json = { key: row[key] for key in row.keys() }
    row_json['text'] = story

    i += 1

    out.write(json.dumps(row_json) + '\n')

  out.close()
