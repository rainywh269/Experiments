#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sqlite3
import requests
from os import path
from lxml import etree
from urllib2 import unquote

debug = 0

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

def retry(num=3):
    def _(f):
        def __(*args, **kwds):
            retry = num
            while(retry>0):
                try:
                    f(*args, **kwds)
                    break
                except Exception as err:
                    print err
                    retry -= 1
        return __
    return _


class Post(object):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    @classmethod
    def commit(cls):
        cls.conn.commit()

    @classmethod
    def rollback(cls):
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

def handle_img_url(url, name=None, folder="imgs"):
    id = name or url
    if Post.insert(id):
        try:
            req = requests.get(url=url)
            if req.status_code == requests.codes.ok:
                filename = unquote(path.split(url)[-1])
                with open('%s/%s' % (folder, filename), 'wb') as f:
                    f.write(req.content)
                print "OK", url
                Post.commit()
                return True
        except:
            pass

    print "fail". url
    Post.rollback()

@retry(3)
def parse_konchan():
    url = "http://konachan.com/post/atom"
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
            handle_img_url(url)

@retry(3)
def parse_melc():
    img_finder = re.compile('src="(.*)"')
    url = "http://melc.tumblr.com/rss"
    if debug:
        text = open("atom").read()
        link = etree.XML(text)
    else:
        req = requests.get(url=url, proxies=proxies)
        link = etree.XML(req.text.encode('utf8'))

    links = link.xpath('//item/description/text()') 

    for link in links:
        urls = img_finder.findall(link)
        for url in urls:
            url = url.replace("_500", "_1280")
            handle_img_url(url, folder="melc") 

def main():
    parse_melc()
    parse_konchan()

if __name__ == '__main__':
    main()
