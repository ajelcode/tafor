# -*- coding: utf-8 -*-
import os
import datetime

from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.schema import ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from config import Config


# 创建对象的基类:
Base = declarative_base()

class Tafor(Base):
    __tablename__ = 'tafors'
    id = Column(Integer, primary_key=True)
    tt = Column(String(2))
    head = Column(String(255))
    rpt = Column(String(255))
    raw = Column(String(255))
    sent = Column(DateTime, default=datetime.datetime.utcnow)
    confirmed = Column(DateTime)

    # task = relationship('tasks', lazy='dynamic')

    def __init__(self, tt, head, rpt, raw=None):
        self.tt = tt
        self.head = head
        self.rpt = rpt
        self.raw = raw

    def __repr__(self):
        return '<TAF %r %r>' % (self.tt, self.rpt)


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    tt = Column(String(2))
    head = Column(String(255))
    rpt = Column(String(255))
    created = Column(DateTime, default=datetime.datetime.utcnow)
    plan = Column(DateTime)

    tafor_id = Column(Integer, ForeignKey('tafors.id'))

    def __init__(self, tt, head, rpt, plan):
        self.tt = tt
        self.head = head
        self.rpt = rpt
        self.plan = plan

    def __repr__(self):
        return '<Task TAF %r %r %r>' % (self.tt, self.rpt, self.plan)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(8))
    phone_number = Column(String(20))

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def __repr__(self):
        return '<User %r %r>' % (self.name, self.phone_number)


# 初始化数据库连接:
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=False)
# 创建DBSession类型:
Session = sessionmaker(bind=engine)
# 创建表
Base.metadata.create_all(engine)