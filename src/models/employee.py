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
    name = Column(String(10),nullable=False)
    phone = Column(String(11),nullable=False)
    wchat = Column(String(30))
    address = Column(String(120))
    birthday = Column(Date())
    password= Column(String(20),nullable=False)
    sex=Column(Enum('man','women'))
    role=Column(Integer, ForeignKey('role.id'))
    comments = Column(String(200))
    
    coach_Info = relationship("Member",primaryjoin="Employee.id==Member.coach_id",backref="employees")

