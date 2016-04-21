#-*- encoding: utf-8 -*-
'''
Created on 2016年4月17日

@author: Bob Yum
@module: src.models.course
'''
from src.models.database import BaseModel
from sqlalchemy import Column,VARCHAR,Integer,DateTime,UnicodeText,ForeignKey
from sqlalchemy.orm import relationship

class TypeCode:
    Team = 'a'
    Private = 'b'

class Course(BaseModel):

    __tablename__ = 'Course'
    CourseId = Column('CourseId', Integer,primary_key=True,nullable=False,autoincrement=True) #课程号
    CType = Column('Type', VARCHAR(4),nullable=False) #课程类型  a为团课 b为私教
    Name = Column('Name', VARCHAR(40),nullable=False) #课程名称
    Duration = Column('Duration', Integer,nullable=False) #时长
    Amount = Column('Amount', Integer,nullable=False) #预约人数
#     Coach = relationship('Member') #教练
    HourFee = Column('HourFee', Integer,nullable=False) #课时费
    Comment = Column('Comment', VARCHAR(100)) #备注
    Description = Column('Description', UnicodeText) #课程介绍
    Creator = Column('Creator', Integer,ForeignKey('UserProfile.UserId'),nullable = False)
    CreateDate = Column('CreateDate', DateTime,nullable=False)
    Modifier = Column('Modifier', Integer,ForeignKey('UserProfile.UserId'),nullable = False)
    LastUpdateDate = Column('LastUpdateDate', DateTime)
    
    
class Plan(BaseModel):

    __tablename__ = 'Plan'
    PlanId = Column('PlanId', Integer,primary_key=True,nullable=False,autoincrement=True) #排课号
    PType = Column('Type', VARCHAR(4),nullable=False) #排课类型  a为团课 b为私教
    CourseId = Column('CourseId', Integer,ForeignKey('Course.CourseId'),nullable = False)
    Course = relationship("Course", foreign_keys=CourseId,primaryjoin=CourseId == Course.CourseId) #课程名称
#     Yard = relationship("Yard") #场地名称
#     Coach = relationship('Member') #教练
    BeginDate = Column('BeginDate', DateTime,nullable=False) #开始日期
    EndDate = Column('EndDate', DateTime,nullable=False) #结束日期
    WorkTime = Column('BeginTime', VARCHAR(4)) #教练上班时间
    OffTime = Column('EndTime', VARCHAR(4)) #教练下班时间
    WeekSchedule = Column('WeekSchedule', VARCHAR(130),nullable=False) #上课安排：团课为四位上课时间加&字符加字符abcdefg代表的星期一至七中上课日期，多组安排以符号^连接   私教为字符abcdefg代表的星期一至七中上课日期
    Creator = Column('Creator', Integer,ForeignKey('UserProfile.UserId'),nullable = False)
    CreateDate = Column('CreateDate', DateTime,nullable=False)
    Modifier = Column('Modifier', Integer,ForeignKey('UserProfile.UserId'),nullable = False)
    LastUpdateDate = Column('LastUpdateDate', DateTime)
    
    
    
    