#-*- encoding: utf-8 -*-
'''
Created on 2016年4月17日

@author: Bob Yum
@module: src.models.order
'''
from src.models.database import BaseModel
from sqlalchemy import Column,VARCHAR,Integer,DateTime,UnicodeText,ForeignKey,DECIMAL
from sqlalchemy.orm import relationship

    
class Goods(BaseModel):

    __tablename__ = 'Goods'
    GoodsId = Column('GoodsId', Integer,primary_key=True,nullable=False,autoincrement=True) #商品ID
    Name = Column('Name', VARCHAR(40),nullable=False) #商品名称
    Price = Column('Price', DECIMAL(10, 2),nullable=False) #加个
    DefaultRebate = Column('Rebate', Integer,default=100) #实际折扣 
    Creator = Column('Creator', Integer,ForeignKey('UserProfile.UserId'),nullable = False)
    CreateDate = Column('CreateDate', DateTime,nullable=False)
    Modifier = Column('Modifier', Integer,ForeignKey('UserProfile.UserId'),nullable = False)
    LastUpdateDate = Column('LastUpdateDate', DateTime)
    

class OrderStatus:
    All = 0  #全部
    Paid = 1    #支付完成
    Cancel = 2    #已取消
    Confirm = 3    #待确认
    TobePay = 4    #待支付 
    Refund = 5    #退款成功
    Refunding = 6    #退款中
    ConfirmAndRefund = 7    #待确认收款后退款
    

class PayMode:
    All = 0  #全部
    Wechat = 1    #微信
    Alipay = 2    #支付宝
    Bank = 3    #银行
    
   
class OrderType:
    All = 0  #全部
    Member = 1    #会员
    Activity = 2    #活动
    Bang = 3    #多人
    
    
class Order(BaseModel):

    __tablename__ = 'Order'
    OrderId = Column('OrderId', Integer,primary_key=True,nullable=False,autoincrement=True) #订单序号
    Member = relationship('Member') #会员
    PayMode = Column('PayMode', Integer,nullable=False) #支付方式    
    PayStatus = Column('PayStatus', Integer,nullable=False) #支付状态
    OrderType = Column('OrderType', Integer,nullable=False) #订单类型
    Goods = relationship('Goods') #商品
    Course = relationship('Course') #课程
    Amount = Column('Amount', Integer,default=1) #数量
    Rebate = Column('Rebate', Integer,default=100) #实际折扣 
    Comment = Column('Comment', VARCHAR(100)) #备注
    Operator = Column('Operator', Integer,ForeignKey('UserProfile.UserId'),nullable = False)
    CreateDate = Column('CreateDate', DateTime,nullable=False)

    
    