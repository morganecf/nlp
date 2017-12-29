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
  output_file = sys.argv[2]
except IndexError:
  print('Input directory and output file are required')
  sys.exit(1)

files = [f for f in os.listdir(input_data_dir) if f.endswith('.txt')]

data = {
  'text': [],
  'category': [],
  'title': []
}

for file in files:
  stories = open(os.path.join(input_data_dir, file)).read().splitlines()

  category  = file.replace('.txt', '')

  print('Category:', category)

  for story in stories:
    story = json.loads(story)
    text = story['text']
    title = story['story_url'].split('/')[-1]
    sentences = sent_tokenize(text)
    data['text'].extend(sentences)
    data['category'].extend([category] * len(sentences))
    data['title'].extend([title] * len(sentences))


print('saving', len(data['text']), 'sentences')
df = pd.DataFrame(data)
df.to_csv(output_file)
