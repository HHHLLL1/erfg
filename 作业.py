# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 16:33:06 2017

@author: Lenovo
"""

import urllib
import re

x=0
        
def getlmg(html):
    global x
    red=r'src="(.*?\.jpg)"'
    imgre=re.compile(red)
    html=html.decode('utf-8')
    imglist=re.findall(imgre,html)
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'F:\%s.jpg'%x)
        x+=1
        print("完成第%s张"%x)
    return imglist

for y in range(2,5):
    url=urllib.request.urlopen('http://www.woyaogexing.com/touxiang/fengjing/index_%s.html'%y)
    html=url.read()
    getlmg(html)
