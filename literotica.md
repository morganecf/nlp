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

Distribution of stories per category: 
![image](https://user-images.githubusercontent.com/4405597/34448248-a19eb6ec-ecb9-11e7-8155-13fb3019d71c.png)  

Most common words across all categories (`ch` and `pt` respectively referring to `chapter` and `part`):
 ```
 [('ch', 90501),
 ('pt', 10034),
 ('love', 4231),
 ('night', 3545),
 ('new', 3276),
 ('day', 3124),
 ('sex', 2854),
 ('first', 2713),
 ('girl', 2548),
 ('time', 2512),
 ('two', 2465),
 ('wife', 2356),
 ('story', 2269),
 ('fun', 2183),
 ('one', 2086),
 ('man', 1845),
 ('young', 1836),
 ('fantasy', 1712),
 ('good', 1614),
 ('life', 1509)]
 ``` 
 
Distribution of popular words across gay vs. lesbian stories:  
![image](https://user-images.githubusercontent.com/4405597/34448286-ec7bacec-ecb9-11e7-84c1-72854c255a95.png)
![image](https://user-images.githubusercontent.com/4405597/34448302-02a06738-ecba-11e7-877e-7df9c3a0b8f6.png)

Most popular words in science fiction / fantasy stories:
![image](https://user-images.githubusercontent.com/4405597/34448314-11ce0e7c-ecba-11e7-9811-a48419137af1.png)

Vaguely amusing titles from a naive title generator:  
```
Licentious Ecclesiastes
Blooming Elf Identity
Overflowing Each Funk Seance
Every Cheese Red
Haughty Butts
Laserdick Submissions
```  

[Interactive D3 network visualization](https://github.com/morganecf/nlp/blob/master/notebooks/Literotica%20Category%20Network.ipynb) linking categories based on author activity:  

<img src="https://user-images.githubusercontent.com/4405597/34368502-8ad7ae48-ea82-11e7-8fac-ee9056a7a285.png" width=400 height=300>

An edge between two categories is weighted by the number of times authors posted a story to both categories (not necessarily the same story -- this just captures author activity across categories).  

### Intensity shapes

Using a [model trained to discriminate between sexual and non-sexual language](https://github.com/morganecf/orb-of-disquiet), sentences from stories across categories were scored so that intensity series could be plotted. Note that this analysis was done on only 1% of the data. 

Sorting categories by average intensity across all their stories:  
![image](https://user-images.githubusercontent.com/4405597/34448364-8ad30f7a-ecba-11e7-8fd6-ff52bcbd9d0d.png)

Estimating intensity probability density across categories:  
![image](https://user-images.githubusercontent.com/4405597/34448373-9a7f3bec-ecba-11e7-9ea9-d7bb2ae13dd6.png)  
The skewed bimodality seems to indicate that the language is more non-erotic than erotic. 

### Word representations across categories

### Classifying story categories

### Building language models

### Generating new stories
