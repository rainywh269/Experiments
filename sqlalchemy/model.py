#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy import MetaData,Table
from sqlalchemy.orm import mapper, sessionmaker, composite
from sqlalchemy.ext.sqlsoup import SqlSoup

engine = create_engine("mysql://root:intelkamd@localhost/test_wooparadog9010")
#engine = create_engine("sqlite:///:memory:")
Base = declarative_base(engine)

class NameMixIn(DeclarativeMeta):
    def __new__(cls, name, bases, attrs):
        if name == 'Base':
            return super(NameMixIn, cls).__new__(cls, name, bases, attrs)
        new_class = super(NameMixIn,cls).__new__(cls,name, bases,attrs)
        new_class.__tablename__ = name.lower()
        new_class.__table_args__ = {'autoload':True}
        return new_class

class Vote(Base):
    __metaclass__ = NameMixIn

def get_session2():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def get_session():
    meta = MetaData(engine)
    ta = Table('vote',meta,autoload=True)
    mapper(Vote,ta)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

if __name__ == '__main__':
    Base.metadata.create_all()
    session = get_session2()
    import ipdb
    ipdb.set_trace()
    print dir(Vote.title)
    #db = SqlSoup(engine)
    #for i in db.vote.all():
    #    print i

    for i in session.query(Vote).all():
        print dir(i)
        print i

    #v = Vote()
    #v.creator_id = 1
    #v.creator_kind = 1
    #v.target_id = 1
    #v.target_kind = 1
    #v.title = 'd'
    ##creator_id, bbbcreator_kind, target_id, target_kind, title, profile)
    #session.add(v)
    #session.commit()
