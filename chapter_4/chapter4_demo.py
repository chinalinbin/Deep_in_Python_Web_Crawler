# -*- coding:utf-8 -*-

import urllib.request


file = urllib.request.urlopen("http://wwww.baidu.com")
# data = file.read()
# dataline = file.readline()
# datalines = file.readlines()
# print(data)
# print(dataline)
# print(datalines)
#
# fhandle = open("D:/Study_Python_Practice/Deep_in_Python_Web_Crawler/Test1.html","wb")
# fhandle.write(data)
# fhandle.close()


# filename = urllib.request.urlretrieve("http://edu.51cto.com",filename = "D:/Study_Python_Practice/Deep_in_Python_Web_Crawler/Test2.html")
# print(file.getcode())
# print(file.info())
# print(file.geturl())

url = "http://blog.csdn.net/weiwei_pig/article/details/51178226"
file = urllib.request.urlopen(url)
headers = ("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read()
print(data)
fhandle = open("D:/Study_Python_Practice/Deep_in_Python_Web_Crawler/chapter_4/Test3.html","wb")
print(fhandle.write(data))
fhandle.close()
