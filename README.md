# NLP projects & notes

## Story analysis

### Downloading data
To download data from [Literotica](https://www.literotica.com) use these commands:  

```
# Saves urls and some metadata for each story to tsv file
python get_literotica_urls.py --urls urls.tsv

# Downloads stories or subset of stories
python download_literotica_data.py --urls urls.tsv --data_dir data/literotica/ --sample 0.2
```  

### Exploration
EDA done in [this notebook]().

### Intensity shapes

### Classifying story categories

### Building language models

### Generating new stories
