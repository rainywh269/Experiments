#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
main.py
Author: WooParadog
Email:  Guohaochuan@gmail.com
Created on
2011-11-24
'''
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from private_config import CONNECTION_STRING

Base = declarative_base()
class modelA(Base):
    """docstring for modelA"""
    def __init__(self, name):
        self.name = name
    __tablename__ = 'hello'
    id = sqlalchemy.Column(sqlalchemy.INTEGER,primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)

if __name__ == '__main__':
    engine = sqlalchemy.create_engine(CONNECTION_STRING)
    print [str(i) for i in engine.execute("select * from hello")]
    Session = sessionmaker(bind=engine)
    session = Session()
    #newU = modelA(name='shit') 
    #session.add(newU)
    #print [str(i) for i in session.query(modelA)]
    for i in session.query(modelA):
        session.delete(i)
        #del i
    #print session.query(modelA)
    session.commit()
