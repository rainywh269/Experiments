#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
parser.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2012-06-04
'''
from lxml.etree import tostring
from lxml import etree
import glob
from collections import defaultdict
from fanjian import ftoj
import yaml

def main():
    files = glob.glob('tmp/*')
    cats = defaultdict(list)
    for file_path in files:
        with open(file_path) as f:
            a = defaultdict(str)
            content = f.read()
            content = content.decode('BIG5')

            parser = etree.HTML(content)
            it = parser.xpath('//body/table')[2]
            title = it.xpath('.//table')[0].xpath('.//table')[0].xpath('.//th//text()')
            #first is normal, else alias
            if len(title) > 1:
                alias = ','.join(title[1:])
            else:
                alias = ''
            title = title[0] if title else 'None'

            ps = it.xpath('.//p/text()')
            cat = parser.xpath('//div[@id="divStayTopRight"]//font[@class="header_s"]/a/text()')
            cat = ','.join(cat) or 'None'
            cat = ftoj(cat).replace(":","：".decode("utf8"))

            ps = filter(unicode, ps)
            ps = filter(lambda x:x.strip(), ps)

            ps.insert(0,'【概述】'.decode('utf8'))
            ps = ''.join(ps)

            # 分段的..她不要
            #current_key = '【概述】'.decode('utf8')
            #for i in ps:
            #    if '【'.decode('utf8') in i:
            #        current_key = ftoj(i)
            #        continue
            #    a[current_key] += ftoj(i)

            a['title'] = ftoj(title).replace(":","：".decode("utf8"))
            a['alias'] = ftoj(alias).replace(":","：".decode("utf8"))
            a['content'] = ftoj(ps).replace(":","：".decode("utf8"))

            cats[cat].append(a)
            if cat == 'None':
                print cat, file_path
    return cats

def str_(cats):
    i = 0
    result = []
    for k, v in cats.items():
        result.append( str(i) + ':')
        result.append(' '*4 + k +':')
        for disease in v:
            result.append( ' '*8 + '%s : %s' %(disease['title'], disease['content']))
        i += 1

    with open('result', 'w') as f:
        f.write("\n".join(result).encode("utf8"))




if __name__ == '__main__':
    txt = main()
    str_(txt)
