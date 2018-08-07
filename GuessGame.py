#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 02:47:53 2018

@author: nikeshkumar
"""

import os
from PIL import Image

myDict = {}

myFolders = [d for d in os.listdir('./DataFiles') if os.path.isdir(os.path.join('./DataFiles', d))]
print(myFolders)

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".jpg") or file.endswith(".png"):
             print(os.path.splitext(os.path.basename(os.path.normpath(os.path.join(root, file))))[0])
             print(os.path.join(root, file))
             myDict[os.path.splitext(os.path.basename(os.path.normpath(os.path.join(root, file))))[0]] = os.path.join(root, file)

image = Image.open('./DataFiles/MovieActors/Chris Hemsworth.jpg')
image.show()