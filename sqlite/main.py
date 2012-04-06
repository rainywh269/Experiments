#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
main.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2012-03-29
'''
import sqlite3
def main():
    conn = sqlite3.connect("/tmp/test")
    c = conn.cursor()

    c.execute("delete from stocks")
    c.execute("""insert into stocks
                      values ('2006-01-05','BUY','RHAT',100,35.14)""")

    # Save (commit) the changes
    conn.commit()

    find = c.execute("select * from stocks")
    al = find.fetchall()
    for i in al:
        print i

if __name__ == '__main__':
    main()
