#-*- coding:utf-8 -*-
import time
import urllib2
import urllib
from sys import argv
 
script,zh,tk = argv

url = "https://translate.google.cn/translate_tts?ie=UTF-8&q="+zh+"&tl=en&total=1&idx=0&textlen=7&tk="+tk+"&client=t"
def getRes():
	#print 'chinese is :'+urllib.unquote(first)
	
        print url
	null_proxy_handler = urllib2.ProxyHandler({})
	opener = urllib2.build_opener(null_proxy_handler)
	urllib2.install_opener(opener)

	req = urllib2.Request(url) 
	req.add_header('User-Agent', "Mozilla/5.0")

	response = urllib2.urlopen(req)
        data = response.read()
        with open("test.mp3", "wb") as f:
            f.write(data)

getRes()
