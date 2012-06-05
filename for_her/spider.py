#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
spider.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2012-06-04
'''
import time
import requests
url_h = "http://yibian.hopto.org/diag/ill/?illno=%s"
headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Charset":"ISO-8859-1,utf-8;q=0.7,*;q=0.3",
        "Accept-Language":"en,en-US;q=0.8,zh-CN;q=0.6,zh;q=0.4",
        "Cache-Control":"max-age=0",
        "Connection":"keep-alive",
        "Host":"yibian.hopto.org",
        "User-Agent":"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1155.2 Safari/537.1",
        }
def main():
    for i in range(1762 , 2504):
        url = url_h%i
        print url
        r = requests.get(url=url, headers=headers)
        time.sleep(5)
        with open("tmp/%s"%i,'w') as f:
            f.write(r.content)

if __name__ == '__main__':
    main()
