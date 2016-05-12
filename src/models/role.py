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
    MEMBER_MANAGE = 0x01 
    COURSE_MANAGE = 0x02
    PRODUCT_ADD = 0x04
    PRODUCT_SEARECH = 0x08

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