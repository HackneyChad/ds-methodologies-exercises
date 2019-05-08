import pandas as pd
import os
import re
import requests
from requests import get
from bs4 import BeautifulSoup
from pathlib import Path
import numpy as np
import unicodedata
import nltk
nltk.download('wordnet')
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
from pprint import pprint

import acquire_blogs
from acquire_blogs import get_blog_articles
from acquire_blogs import get_all_codeup_articles


# Performs lowercase, normalize, remove anything that's not letter/number/whitespace/underscores.
def basic_clean(string):
    string = string.lower()
    string = unicodedata.normalize('NFKD', string).encode('ascii','ignore').decode('utf-8','ignore')
    string = re.sub(r'\s', ' ', string)
    string = re.sub(r"[^a-z0-9\s\n]", '', string)    
    return string

#Returns a tokenized version of the string.
def tokenize(string):
    tokenizer = nltk.tokenize.ToktokTokenizer()
    return tokenizer.tokenize(string, return_str=True)

#Performs stemming on the string.
def stem(string):
    ps = nltk.stem.PorterStemmer()
    stems = [ps.stem(word) for word in string.split()]
    content_stemmed = ' '.join(stems)
    return content_stemmed

#Performs lemmatize on the string.
def lemmatize(string):
    wnl = nltk.stem.WordNetLemmatizer()
    lemmas = [wnl.lemmatize(word.lower()) for word in string.split()]
    content_lemmatized = ' '.join(lemmas)
    return content_lemmatized


def remove_stopwords(string):
    stopword_list = stopwords.words('english')
    stopword_list.remove('no')
    stopword_list.remove('not')
    words = string.split()
    filtered_words = [w for w in words if w not in stopword_list]
    article_without_stopwords = ' '.join(filtered_words)
    return article_without_stopwords.lower()


def prep_article(article):
    output = {
        'title': article['title'],
        'original': article['content'],
        'stemmed': stem(article['content']),
        'lemmatize': lemmatize(article['content']),
        'clean': basic_clean(article['content']),
        'stopped': remove_stopwords(article['content'])
    }
    return output

def prepare_article_data():
    articles = acquire_blogs.get_all_codeup_articles()
    prepped_articles = [prep_article(article) for article in articles]
    return prepped_articles

#prepped_articles = 
pprint(prepare_article_data())