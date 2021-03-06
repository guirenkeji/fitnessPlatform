'''
Created on Apr 14, 2016

@author: Bruce
'''
from src.models.database import BaseModel

from sqlalchemy import Column, Integer, String,Date,Sequence
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey
from sqlalchemy import *


class Member(BaseModel):
    '''
    Member model
    '''
    
    __tablename__ = 'members'
    id = Column(Integer, primary_key=True)
    name = Column(String(50),nullable=False)
    phone = Column(String(11),nullable=False)
    wchat = Column(String(30))
    address  = Column(String(100))
    role=Column(Integer, ForeignKey('role.id'))
    sex=Column(Enum('man','women'))
    birthday = Column(Date())
    expenses_not_quota_password= Column(String(20),nullable=False)
    expenses_quota=Column(Integer)
    expenses_not_quota=Column(Integer)
    course_num = Column(Integer)
    course_num_free = Column(Integer)
    comments = Column(String(200))
    body_info=Column(String(50))
    
    coach_id=Column(Integer, ForeignKey('employees.id'))
    
    


    
        