#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 15:17:20 2018

@author: nshettipalli
"""

import re
import requests
import urllib
from bs4 import BeautifulSoup
count = 0
for i in range(1,11):
    site = 'https://www.imdb.com/list/ls058011111/?sort=list_order,asc&mode=detail&page='
    site = site+''+str(i)
    response = requests.get(site)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    
    urls = [img['src'] for img in img_tags]
    names = [img['alt'] for img in img_tags]
    #print(urls)
    #    if "images/navbar" not in url or "images/nopicture" not in url:
    for url,name in zip(urls,names): 
        if "images/navbar" not in url:
            if "images/nopicture" not in url:
                filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
                urllib.urlretrieve(url,name+'.jpg')
                count+=1
                print(count)
            