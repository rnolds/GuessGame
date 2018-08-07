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
count = 1
flag = True
for i in range(1,101707):
    site = 'https://www.imdb.com/search/name?gender=female&start='+str(count)+'&ref_=rlm'
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
                print(count)
                count+=1
                urllib.urlretrieve(url,name+'.jpg')
                if count==501:
                    flag=False
                    break
                
    if flag==False:
        break
            