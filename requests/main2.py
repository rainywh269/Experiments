#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import re
from bot_txt import txt_wrap_by_all

finder = re.compile('http://.*?(\d+)', re.S|re.M)

s = requests.session()
s.get(url="http://theoden.intra.douban.com:8001/radio")

def get_user_id(user_id):
    r= s.post(url="http://theoden.intra.douban.com:8001/data", data={"user_id":user_id, "rtype":"S","db":"elf_farm","dtype":"radio"})
    return r.content

def get_track_id(track_id):
    r= s.post(url="http://theoden.intra.douban.com:8001/data", data={"track_id":track_id, "dtype":"track"})
    return r.content

if __name__ == '__main__':
    for i in finder.findall(get_track_id(642466)):
        content =  get_user_id(i)
        ids = txt_wrap_by_all('id:','</br',content)
        print ids

