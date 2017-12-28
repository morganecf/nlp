## Literotica Story analysis

### Data
To download data from [Literotica](https://www.literotica.com) use these commands:  

```
# Saves urls and some metadata for each story to tsv file
python get_literotica_urls.py --urls urls.tsv

# Downloads stories or subset of stories
python download_literotica_data.py --urls urls.tsv --data_dir data/literotica/ --sample 0.2
```  
A snapshot of the urls as of 12-24-2017 is available at `data/literotica_urls.tsv`, so skip the first command if you want to use those.  

### Exploration
Basic EDA on category-level stats done in [this notebook](https://github.com/morganecf/nlp/blob/master/notebooks/Literotica%20EDA.ipynb). Some highlighted findings:  

[Interactive D3 network visualization](https://github.com/morganecf/nlp/blob/master/notebooks/Literotica%20Category%20Network.ipynb) linking categories based on author activity:  

<img src="https://user-images.githubusercontent.com/4405597/34368502-8ad7ae48-ea82-11e7-8fac-ee9056a7a285.png" width=400 height=300>

An edge between two categories is weighted by the number of times authors posted a story to both categories (not necessarily the same story -- this just captures author activity across categories).  

### Intensity shapes

### Word representations across categories

### Classifying story categories

### Building language models

### Generating new stories
