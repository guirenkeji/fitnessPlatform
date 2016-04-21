'''
Created on Apr 14, 2016

@author: Bruce
'''
from src.models.database import BaseModel

from sqlalchemy import Column, Integer, String,Date,Sequence
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey
from sqlalchemy import *


class Employee(BaseModel):
    '''
    Employee model
    '''
    
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String(50),nullable=False)
    phone = Column(String(11),nullable=False)
    wchat = Column(String(30))
    address = Column(String(120))
    birthday = Column(Date())
    password= Column(String(20),nullable=False)
    sex=Column(Enum('men','women'))
#     role=Column(Enum('coach','manger','front','other',))
    
    coach_Info = relationship("Member",primaryjoin="Employee.id==Member.coach_id",backref="employees")

class bodyMeasurement(BaseModel):
    __tablename__ = 'body'
    id = Column(Integer, primary_key=True)
    
    body_Info = relationship("Member",primaryjoin="bodyMeasurement.id==Member.body_id",backref="body")

    
class Member(BaseModel):
    '''
    Member model
    '''
    
    __tablename__ = 'members'
    id = Column(Integer, primary_key=True)
    name = Column(String(50),nullable=False)
    phone = Column(String(11),nullable=False)
    wchat = Column(String(30))
    type=Column(Enum('vip','normal'))
    birthday = Column(Date())
    expenses_not_quota_password= Column(String(20),nullable=False)
    expenses_quota=Column(Integer)
    expenses_not_quota=Column(Integer)
    course_num = Column(Integer)
    course_num_free = Column(Integer)
    
    body_id=Column(Integer, ForeignKey('body.id'))
    
    coach_id=Column(Integer, ForeignKey('employees.id'))
    
    


    
        