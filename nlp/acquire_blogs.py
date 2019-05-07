import pandas as pd
import os
import re
import requests
from requests import get
from bs4 import BeautifulSoup
from pathlib import Path

links = ['https://codeup.com/competitor-bootcamps-are-closing-is-the-model-in-danger/',
         'https://codeup.com/why-san-antonio-has-more-than-tacos-to-offer/',
         'https://codeup.com/codeups-data-science-career-accelerator-is-here/',
         'https://codeup.com/data-science-myths/',
         'https://codeup.com/data-science-vs-data-analytics-whats-the-difference/'
        ]

def get_blog_articles(url):
    headers = {'User-Agent': 'Codeup Ada Data Science'}
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.text)
    title = soup.find('title')
    content = soup.find('div', class_='mk-single-content')

    d = dict()
    d['title'] = title.text
    d['content'] = content.text
    return d

corpus = []

for link in links:
    corpus.append((get_blog_articles(link)))