"""
Convert literotica data to csv file, with one paragraph or sentence per row.
This is used for scoring using the hub model.
"""

import os
import sys
import json
import pandas as pd
from nltk.tokenize import sent_tokenize

try:
  input_data_dir = sys.argv[1]
  output_data_dir = sys.argv[2]
except IndexError:
  print('Input and output data directories are required and cannot be the same')
  sys.exit(1)

files = [f for f in os.listdir(input_data_dir) if f.endswith('.txt')]

paragraphs = []

for file in files:
  stories = open(os.path.join(input_data_dir, file)).read().splitlines()
  out_path = os.path.join(output_data_dir, file.replace('.txt', '-sentences.csv'))

  data = []
  for story in stories:
    story = json.loads(story)
    text = story['text']
    sentences = sent_tokenize(text)
    data.extend(sentences)

  print('\tSaving', len(data), 'sentences from category', file)
  df = pd.DataFrame({'text': data})
  df.to_csv(out_path)
