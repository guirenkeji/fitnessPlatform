'''
Created on Apr 14, 2016

@author: Bruce
'''
from src.models.database import BaseModel
from sqlalchemy import Column, Integer, String,Date,Sequence

class Employee(BaseModel):
    '''
    Employee model
    '''
    
    __tablename__ = 'employees'
    id = Column(Integer,Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    phone = Column(String(11))
    wchat = Column(String(30))
    address = Column(String(120))
    birthday = Column(Date())
    password= Column(String(20))


    
        