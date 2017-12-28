# NLP projects & notes

## Story analysis

This repository collects the text and metadata from several online story or fanfiction sources and uses NLP and machine learning techniques to analyze the data and build generative models from the data. The data sources are:  

* Cyberpunk fanfic stories from [Archive Of Your Own](https://archiveofourown.org/tags/Cyberpunk)
* Erotic fiction from [Literotica.com](https://www.literotica.com). See [here](https://github.com/morganecf/nlp/blob/master/literotica.md) for an overview of observations gleaned from the dataset

This README will go over some of the cyberpunk analyses. 

### Data
To download the cyberpunk stories: 

```
# To scrape urls:
python download_cyberpunk_data.py --urls urls.tsv

# To download data (will scrape urls first if urls.tsv is empty):
python download_cyberpunk_data.py --urls urls.tsv --data_dir data/cyberpunk_data/
```  
A snapshot of the urls as of 12-28-2017 is available at `data/cyberpunk_stories_urls.txt`, so skip the first command if you want to use those.  

### Exploration  

### Word representations across categories

### Classifying story categories

### Building language models

### Bootstrapping an existing language model

### Generating new stories
