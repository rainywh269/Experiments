#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import requests
from os import path
from lxml import etree
from urllib2 import unquote

debug = False

url = "http://konachan.com/post/atom"
proxies = {
        "http": "10.8.0.1:8118",
        "https": "10.8.0.1:8118",
            }

current_path = path.dirname(path.abspath(__file__))
DB_FILENAME = "db.sqlite3"
DB_FILE = path.join(current_path, DB_FILENAME)

if not path.exists(DB_FILE):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''create table record(
    url text unique not null)''')
    conn.close()
    
class Post(object):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    @classmethod
    def commit(cls):
        cls.conn.commit()

    @classmethod
    def commit(cls):
        cls.conn.rollback()

    @classmethod
    def insert(self, url):
        try:
            self.cursor.execute("insert into record "
                    "(url) "
                    "values (?)", 
                    (url, ))
            return True
        except Exception, err:
            print err, url
            return False

def main():
    global url
    if debug:
        text = open("atom").read()
        link = etree.XML(text)
    else:
        req = requests.get(url=url, proxies=proxies)
        link = etree.XML(req.text.encode('utf8'))

    links = link.xpath('//n:entry/n:link[@rel="alternate"]/@href', namespaces={"n":"http://www.w3.org/2005/Atom"}) 
    for link in links:
        req = requests.get(url=link, proxies=proxies)
        tree = etree.HTML(req.text)
        pngs = tree.xpath('//a[@id="png"]/@href')
        jpgs = tree.xpath('//a[@id="highres"]/@href')
        result = pngs or jpgs
        for url in result:
            if Post.insert(url):
                try:
                    req = requests.get(url=url)
                    if req.status_code == requests.codes.ok:
                        filename = unquote(path.split(url)[-1])
                        with open('imgs/%s' % filename, 'wb') as f:
                            f.write(req.content)
                        print "OK", url
                    Post.commit()
                except:
                    Post.rollback()

if __name__ == '__main__':
    main()
