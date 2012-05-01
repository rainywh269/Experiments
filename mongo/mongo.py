#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import connection

conn = connection.Connection(host="localhost")

def main():
    db = conn['testdb']
    collection = db['testcollection']
    post = {"asdf":3,"this":5}
    collection.insert(post)

    cursor = collection.find({'asdf':3})
    for i in cursor:
        print i

if __name__ == '__main__':
    main()
