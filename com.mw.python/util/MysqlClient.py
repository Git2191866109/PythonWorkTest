# -*-coding:UTF-8-*-
__author__ = 'chx'

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker

class DbSession:
    def __init__(self, url):
        db_engine = create_engine(url, convert_unicode=True, echo=True, encoding='utf-8')
        print "db_engine: ", db_engine
        self.sm = sessionmaker(bind=db_engine)

    def getSession(self):
        return self.sm
