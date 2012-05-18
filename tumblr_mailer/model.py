#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
model.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2012-05-01
'''

import sqlite3
import oauth2
from configs import CONSUMER_KEY, CONSUMER_SECRET, DB_FILE
from lxml import html
import json


class Client(object):
    def __init__(self, oauth_token, oauth_token_secret):
        consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
        token = oauth2.Token(oauth_token, oauth_token_secret)
        self.client = oauth2.Client(consumer, token)
    
    def get_posts(self, q):
        url = "http://api.tumblr.com/v2/user/dashboard?limit=200%s"%("&since_id=%s"%q if q else "")
        resp, content =  self.client.request(url,"GET")
        content = json.loads(content)
        return content['response']['posts']

class Post(object):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    @classmethod
    def get_unmailed_posts(cls, user_id=0):
        cls.cursor.execute("select * from posts "
                "where user_id=? and state = 0", (user_id,))
        for i in cls.cursor.fetchall():
            yield Post(user_id).from_db(i)

    @classmethod
    def get_max_id(cls, user_id=0):
        cls.cursor.execute("select max(id) from posts where user_id=?", 
                (user_id,))
        max_id = cls.cursor.fetchone()
        return max_id and max_id[0]

    def from_db(self, post):
        self.id, self.url, self.text, self.state, self.type, self.user_id = post
        return self

    def from_post(self, post, user_id=0):
        self.user_id = user_id
        self.post = post
        self.id = post['id']
        self.url = post['post_url']

        return self

    def __init__(self, user_id=0):
        pass

    def update_post_state(self):
        self.cursor.execute("update posts set state=1 where id=?",(self.id,))
        self.commit()

    def commit(self):
        self.conn.commit()

    def _insert(self, text, type, state=0):
        self.cursor.execute("insert into posts "
                "(id, url, text, state, type, user_id) "
                "values (?,?,?,?,?,?)", 
                (self.id, self.url, text, state, self.__class__.__name__, self.user_id))
        self.commit()

    def save(self):
        self._insert(self.text, "text")

class TextPost(Post):
    def __init__(self,post):
        title = post['title'] and post['title'].strip() or "No Title"
        self.text = "<h1>%s</h1>"%title +  post['body'] 
        super(TextPost,self).from_post(post)

    @classmethod
    def get_posts(cls, user_id=0, state=0):
        cls.cursor.execute("select * from posts where user_id=? "
                "and state=? and type=?", 
                (user_id, state, cls.__name__))
        for i in cls.cursor.fetchall():
            yield i

class QuotePost(Post):
    def __init__(self,post):
        self.text = "<h1>%s</h1>"%post['text']
        super(QuotePost,self).from_post(post)

def post_factory(post):
    if post['type'] == 'quote':
        return QuotePost(post)
    elif post['type'] == 'text':
        return TextPost(post)

if __name__ == '__main__':
    result = []
    for i in Post.get_unmailed_posts():
        result.append( i.text)
    text = '\n\n---\n\n'.join(result)
    text = text.encode('utf8')
    print text   
