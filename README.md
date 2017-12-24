# NLP projects & notes

## Story analysis

### Downloading data
Use `scripts/get_literotica_urls.py` and `scripts/download_literotica_data.py` to download data from [Literotica](https://www.literotica.com).  

```
# Saves urls and some metadata for each story to tsv file
python get_literotica_urls.py urls.tsv

# Downloads stories or subset of stories
python download_literotica_data.py --urls urls.tsv --data_dir data/literotica/ --sample 0.2
```  

### EDA
EDA done in [this notebook]().
