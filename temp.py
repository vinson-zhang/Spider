# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html


import re
import requests
import json

url = "http://graph.baidu.com/s?sign=002d51cb543cf6a2cfd86x1554198080&wd=&f=face&srcp=&tn=wise&idctag=nj&sids=10007_10190_10290_10390_10691_10705_10301_10709_10801_10902_11006_10905_10912_11000_10014_10117_10016_10018_11022_11031&logid=2480222939&entrance=&output_verticals=general&client_app_id=15704889&pageFrom=tool&ua="
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
# }
i = 0
while i < 10000:
    # r1 = requests.get(url, headers=headers).text
    r1 = requests.get(url).text
    print r1
    if r1.index("title") < 0:
        print(r1)
        break
    print i
    i = i + 1