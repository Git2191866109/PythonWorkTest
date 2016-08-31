# coding: utf-8
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker

# 创建对象的基类:
Base = declarative_base()


#  table 下述示例描述了电影同导演的多对一关系。示例中说明了从用户定义的Python类创建数据表的方法，双方关系实例的创建方法，以及最终查询数据的方法：包括延迟加载和预先加载两种自动生成的SQL查询。
class Movie(Base):
    # table name
    _table_name_ = 'movies'
    # table column
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    year = Column(Integer, )
    directed_by = Column(Integer, ForeignKey('directors.id'))

    def __int__(self, title=None, year=None):
        self.title = title
        self.year = year

    def __repr__(self):
        return "Movie(%r,%r,%r)" % (self.title, self.year, self.director)


class Director(Base):
    __tablename__ = 'directors'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return "Director(%r)" % (self.name)


# 初始化数据库连接,create_engine()用来初始化数据库连接,'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('dbms://user:pwd@host/dbname')
Base.metadata.create_all(engine)

# 插入的电影和导演对象可以互相引用：# 创建DBSession类型:
Session = sessionmaker(bind=engine)
session = Session()

#
m1 = Movie("Star Trek", 2009)
m1.director = Director("JJ Abrams")

d2 = Director("George Lucas")
d2.movies = [Movie("Star Wars", 1977), Movie("THX 1138", 1971)]

try:
    session.add(m1)
    session.add(d2)
    session.commit()
except:
    session.rollback()
finally:
    session.close()

# search table
alldata = session.query(Movie).all()
for somedata in alldata:
    print somedata
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    # user = session.query(User).filter(User.id=='5').one()
    # 打印类型和对象的name属性:
    # print 'type:', type(user)
    # print 'name:', user.name
