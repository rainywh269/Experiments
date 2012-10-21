#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
from collections import defaultdict

url = "http://ph.futures.hexun.com/module/trader/ajax.shtml?action=fetch_org_data&role=271&page=%s&callback=jsonp1350654479061"

f = open("result.ddd" ,'w')

def main():
    final_datas = []
    for n in range(1,6):
        data = requests.get(url=url%n)
        jsonp = data.content
        jsonp = jsonp[jsonp.find("(")+1:jsonp.find(");")]
        data = json.loads(jsonp)

        data = data['data']
        final_datas.extend(data)

    final_datas.sort(key=lambda x:x['dateline'])
    print >>f, ','.join([k for k in sorted(final_datas[0].keys())])
    for d in final_datas:
        datas = [v for k,v in sorted(d.items())]
        print >>f, ','.join(datas)

if __name__ == '__main__':
    main()
