#-*- coding:utf-8 -*-
import time
import urllib2
import urllib
import sys
import os
from sys import argv
import execjs
import speech_recognition as sr
 
dd = {" ":"%20", "#": "%23", "$": "%24", "%": "%25", "&": "%26", "'": "%27", "+": "%2B", ",": "%2C"}

def encode(txt):
    s = ""
    for x in txt:
        if x in dd:
            s += dd[x]
        else:
            s += x
    return s

def get_mp3(txt, mp3_file):
    tk = ctx.call('gettk', txt)
    txt = encode(txt)
    print txt
    url = "https://translate.google.cn/translate_tts?ie=UTF-8&q="+txt+"&tl=en&total=1&idx=0&textlen=7&tk="+tk+"&client=t"
    print url
    null_proxy_handler = urllib2.ProxyHandler({})
    opener = urllib2.build_opener(null_proxy_handler)
    urllib2.install_opener(opener)

    req = urllib2.Request(url) 
    req.add_header('User-Agent', "Mozilla/5.0")

    response = urllib2.urlopen(req)
    data = response.read()
    with open(mp3_file, "wb") as f:
        f.write(data)

def speech(mp3_file):
    wav_file = mp3_file.split(".")[0] + '.wav'
    if os.path.exists(wav_file):
        os.remove(wav_file)
    cmd = "ffmpeg -i " + mp3_file + " -f wav " + wav_file
    os.system(cmd + "> log 2>&1")
    r = sr.Recognizer()
    with sr.AudioFile(wav_file) as source:
        audio = r.record(source)  
    return r.recognize_sphinx(audio)

    #return r.recognize_google(audio)
    #GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""INSERT THE CONTENTS OF THE GOOGLE CLOUD SPEECH JSON CREDENTIALS FILE HERE"""
    #return r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
    #WIT_AI_KEY = "INSERT WIT.AI API KEY HERE"
    #return r.recognize_wit(audio, key=WIT_AI_KEY)
    #HOUNDIFY_CLIENT_ID = "INSERT HOUNDIFY CLIENT ID HERE"
    #HOUNDIFY_CLIENT_KEY = "INSERT HOUNDIFY CLIENT KEY HERE"
    #return r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY)

f = open("gettk.js", 'r')
line = f.readline()
jsstr = ''
while line:
    jsstr = jsstr + line
    line = f.readline()
ctx = execjs.compile(jsstr)

def main():
    txt = sys.argv[1]
    print txt
    get_mp3(txt, "hello.mp3")
    print speech("hello.mp3")

main()
