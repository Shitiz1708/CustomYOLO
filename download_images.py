import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import json
import requests
import urllib.request

path = './data.json'
f = open(path,'r')
count = 1
while True:
    line = f.readline()
    if not line:
        break
    # print(line)
    line_json = json.loads(line)
    # print(line_json)
    # print(line_json['content'])
    if(line_json['annotation'][0]['label'][0]=='Plate'):
        print(line_json['content'])
        print(count)
        urllib.request.urlretrieve(line_json['content'], "./plate_images/" + str(count) + ".jpg")
        count+=1