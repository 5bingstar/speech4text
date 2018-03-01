#-*- coding:utf-8 -*-
import os

# 爬取网页拿到TKK的js代码
os.system('python getTKKjs.py > getTKK.js')  

# 执行TKKjs代码拿到TKK值
os.system('node getTKK.js > TKK')
