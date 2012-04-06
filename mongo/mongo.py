#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import connection

conn = connection.Connection(host="localhost")

def main():
    db = conn.dfgb
    print db.dddd

if __name__ == '__main__':
    main()
