# -*- coding: UTF-8 -*- 
'''
Created on Apr 24, 2016

@author: Bruce
'''
from src.models.database import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Permission:
    """
    Permission
    """
    NO_PERMISSION =0x00
    SELF_READ = 0x01 
    SELF_WRITE = 0x02
    MEMBER_READ = 0x04
    MEMBER_WRITE = 0x08
    EMPLOYEE_READ = 0x10
    EMPLOYEE_WRITE = 0x20
    ACCOUNTING_READ = 0x40
    ACCOUNTING_WRITE = 0x80
    CROSS_SITE = 0x100

class Role(BaseModel):
    """
    Role
    """
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    name = Column(String(164))
    
    permissions = Column(Integer,default=Permission.NO_PERMISSION)
    taozhang=Column(String(10),default='杭州')
    comments=Column(String(200))
    

   
if __name__ == '__main__':
    pass