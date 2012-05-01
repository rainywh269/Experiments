#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
main.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2012-05-01
'''

from model import Client, post_factory, Post
from configs import OAUTH_TOKEN, OAUTH_TOKEN_SECRET

def main():
    client = Client(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    max_id = Post.get_max_id()
    for post in client.get_posts(max_id):
        post = post_factory(post)
        if post:
            post.save()

if __name__ == '__main__':
    main()
