# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 17:12:08 2019

@author: dell
"""

import requests
import re
print("开始爬虫")
content = requests.get('https://book.douban.com/').text
#url = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>',re.S)
url = re.compile('<li.*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>',re.S)
results = re.findall(url,content)
for each in results:
    name,author,data=each
    print(name,author,data)