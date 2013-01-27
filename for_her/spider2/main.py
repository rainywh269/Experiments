#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2013 wooparadog <wooparadog@1l0v3U4v3r>
#
# Distributed under terms of the MIT license.

import os
import re
import requests
import cPickle
import hashlib
upload_url = "http://knowminer.at:8080/team-pdf-extraction-webapp/extract/?action=upload"
result_extractor = re.compile("<h\d>(.*)<div", re.S|re.M)
block_splitter = re.compile("<h\d>")
block_end_splitter = re.compile("</h\d>")
list_item_finder = re.compile("<li>(.*?)</li>")
cache_dir = "cache"


def cache(content_getter):
    def __(f):
        if not os.path.exists(cache_dir):
            os.mkdir(cache_dir)

        def key_builder(*arg, **kwds):
            raw_key = '_'.join(list(arg)+["%s_%s" % (k, v) for k, v in kwds.iteritems()])
            key = hashlib.md5()
            key.update(raw_key )
            return key.hexdigest()

        def _(*arg, **kwds):
            key = key_builder(*arg, **kwds)
            cache_path = os.path.join(cache_dir, key)
            if os.path.exists(cache_path):
                try:
                    result = cPickle.load(open(cache_path))
                except:
                    print "cache miss, reuploading"
                else:
                    print "cache hit"
                    return result

            result = f(*arg, **kwds)
            with open(cache_path, 'w') as fp:
                content = content_getter(result)
                fp.write(cPickle.dumps(content))
            return content
        return _
    return __

@cache(lambda x:x.text)
def upload(pdf_file):
    try:
        files = {
                "file": open(pdf_file)
                }
    except IOError:
        print "file io error"
    else:
        return requests.post(upload_url, files=files)

def ul_to_list(html):
    """
    >>> ul_to_list("<ul><li>1.a</li><li>2.b</li></ul>")
    ['1.a', '2.b']
    >>> ul_to_list("asdfas asd fas df ")
    'asdfas asd fas df '
    """
    return list_item_finder.findall(html) or html
    

def parse_result(content):
    html = content
    content = result_extractor.findall(html)
    result = {}
    if content:
        content = content[0]
        for block in block_splitter.split(content):
            meta = block_end_splitter.split(block, 1)
            k, v = meta
            result[k.strip()] = ul_to_list(v.strip())

    return result

def analysis_pdf(pdf_file):
    content = upload(pdf_file)
    result = parse_result(content)
    return result


def main():
    test_pdf_file_path = "/home/wooparadog/Dropbox/books/Papers/PDF4test/S10-8.pdf"
    result = analysis_pdf(test_pdf_file_path)
    for k, v in result.iteritems():
        print "++++++++++++++"
        print k
        print "--------------"
        print v

if __name__ == '__main__':
    #import doctest
    #doctest.testmod()

    main()
