#-*- encoding: utf-8 -*-
'''
Created on 2016年4月18日

@author: Bob Yum
@module: src.models.venue
'''
from src.models.database import BaseModel
from sqlalchemy import Column,NVARCHAR,VARCHAR,Integer,DateTime,ForeignKey
from sqlalchemy.orm import relationship

class UsageStatus:
    Team = 'a'
    Private = 'b'
    TAndP = 'ab'

class Venue(BaseModel):

    __tablename__ = 'Venue'   #场馆
    VenueId = Column('VenueId', Integer,primary_key=True,nullable=False,autoincrement=True)
    Name = Column('Name', VARCHAR(40),nullable=False)
    PhoneNo = Column('PhoneNo', NVARCHAR(21),nullable=False)
    Address = Column('Address', VARCHAR(255),nullable = False)
    Email = Column('Email', VARCHAR(40),nullable=False)
    Priority = Column('Priority', Integer,nullable=False)
    Creator = Column('Creator', Integer,ForeignKey('UserProfile.UserId'),nullable = False)
    CreateDate = Column('CreateDate', DateTime,nullable=False)
    Modifier = Column('Modifier', Integer,ForeignKey('UserProfile.UserId'),nullable = False)
    LastUpdateDate = Column('LastUpdateDate', DateTime)

class Yard(BaseModel):  

    __tablename__ = 'Yard'  #场地
    YardId = Column('YardId', Integer,primary_key=True,nullable=False,autoincrement=True)
    Venue = Column('Venue', Integer,ForeignKey('Venue.VenueId'),nullable = False)
    YardName = Column('YardName', VARCHAR(255),nullable=False)  
    Galleryful = Column('Galleryful', Integer,nullable=False)  #容纳人数
    Usage = Column('Usage', Integer,nullable=False) #用途  值为'a','b'或'ab'
    Creator = Column('Creator', Integer,ForeignKey('UserProfile.UserId'),nullable = False)
    CreateDate = Column('CreateDate', DateTime,nullable=False)
    Modifier = Column('Modifier', Integer,ForeignKey('UserProfile.UserId'),nullable = False)
    LastUpdateDate = Column('LastUpdateDate', DateTime)


    