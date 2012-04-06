#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import argparse
#from BeautifulSoup import BeautifulSoup

def main():
    parser = argparse.ArgumentParser(description="PPP")
    parser.add_argument('-k','--keys')
    parser.add_argument('-w','--words')
    args = parser.parse_args()
    keys = args.keys.split()
    words = args.words.split()
    headers = {
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Charset":"ISO-8859-1,utf-8;q=0.7,*;q=0.3",
            "Accept-Encoding":"gzip,deflate,sdch",
            "Accept-Language":"en,en-US;q=0.8,zh-CN;q=0.6,zh;q=0.4",
            "Avail-Dictionary":"D-t65Pri",
            "Connection":"keep-alive",
            "Host":"www.google.com",
            "Referer":"http://www.google.com",
            "User-Agent":"Mozilla/5.0 (X11; Linux i686) AppleWebKit/536.4 (KHTML, like Gecko) Chrome/19.0.1077.3 Safari/536.4",
            }
    
    s = requests.session()
    r = s.get(url="http://google.com/ncr")

    url = "https://www.google.com/search"
    payload = dict(
            channel="fs",
            ie="utf-8",
            oe="utf-8",
            hl="en",
            )

    result = {}
    import itertools
    for i in keys:
        payload['q'] = i
        r = s.get(url, params=payload)
        print zip(filter(lambda x:x in r.text ,words),[r.url])

        
        #soup = BeautifulSoup(r.text)
        #wrapper = soup.find(id='subform_ctrl')
        #print wrapper.findAll('div')[-1].text.split()[1].replace(',','')
        #raw_input()

if __name__ == '__main__':
    main()
