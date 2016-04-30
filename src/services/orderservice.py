#-*- encoding: utf-8 -*-
'''
Created on 2016年4月21日

@author: Bob Yum
@module: src.services.orderservice
'''
from src.models import database,Course,Plan,Member,Yard,Order,Goods
from datetime import datetime
# from decimal import Decimal
# import json


def confirm_order(OrderId):#确认订单  PayStatus=1的订单为交易完成的订单  只有PayStatus=3即待确认的订单有次操作
    session = database.get_session()
    order = session.query(Order).filter(Order.OrderId == OrderId).first()
    if order.PayStatus!=3:
        session.close()
        return False
    order.PayStatus = 1
    session.commit()
    session.close()
    return True

def cancel_order(OrderId):#取消订单  只有 PayStatus为1,3,4的订单（待支付,确认或已完成的）为可取消的订单
    session = database.get_session()
    order = session.query(Order).filter(Order.OrderId == OrderId).first()
    if order.PayStatus not in (1,3,4):
        session.close()
        return False
    if order.PayStatus == 1:
        order.PayStatus = 6
    elif order.PayStatus == 3:
        order.PayStatus = 7
    else:
        order.PayStatus = 2
    session.commit()
    session.close()
    return True

def pay_order(OrderId):#支付订单  只有 PayStatus为4的待支付订单才可以 “支付订单”
    session = database.get_session()
    order = session.query(Order).filter(Order.OrderId == OrderId).first()
    if order.PayStatus!=4:
        session.close()
        return False
    order.PayStatus = 3
    session.commit()
    session.close()
    return True

def refund_order(OrderId):#退款  只有PayStatus=6的订单可退款
    session = database.get_session()
    order = session.query(Order).filter(Order.OrderId == OrderId).first()
    if order.PayStatus!=6:
        session.close()
        return False
    order.PayStatus = 5
    session.commit()
    session.close()
    return True

def confirm_and_refund_order(OrderId):#确认并退款  只有PayStatus=7的订单可确认并退款
    session = database.get_session()
    order = session.query(Order).filter(Order.OrderId == OrderId).first()
    if order.PayStatus!=7:
        session.close()
        return False
    order.PayStatus = 5
    session.commit()
    session.close()
    return True

def create_fitnessorder(OrderName,OrderType, Price,Amount, BuyName, BuyerName, Comment):
    session = database.get_session()
    
    
    o = Order()
    o.PayMode =1
    o.PayStatus =2
    o.Operator = 1
    o.Rebate =1
#     o.OrderId =OrderId
    o.OrderName = OrderName.strip()
#     o.PayMode = PayMode.strip()
    o.OrderType = OrderType.strip()
#     先注释商品和教练关联
#     if Member_id:
#         m = Member()
#         m.UserId = Member_id
#         o.Member.append(m)
#         
#     if Goods_id:
#         g = Goods()
#         g.GoodsId = Goods_id
#         o.Goods.append(g)
#     if Course_id:
#         c = Course()
#         c.Course = Course_id
#         o.Course.append(c)
    o.Amount = int(Amount)
    o.Price = Price
    o.BuyName = BuyName
    o.BuyerName = BuyerName
    o.Comment = Comment.strip()
#     o.Operator = creator
    o.CreateDate = datetime.now()
    session.add(o)
    session.commit()
    session.close()

# def create_goods(Name,Price,DefaultRebate=100,creator):
#     session = database.get_session()
#     g = Goods()
#     g.Name = Name.strip()
#     g.Price = Price
#     g.DefaultRebate = int(DefaultRebate)
#     g.Creator = creator
#     g.CreateDate = datetime.now()
#     session.add(g)
#     session.commit()
#     session.close()
    
def query_order(page_no,page_size,order_by,current_user,PayMode=0,OrderType=0,PayStatus=0):
    session = database.get_session()
    subdata = session.query(Order).filter(Order.Operator == current_user).filter(Order.PayMode == PayMode).filter(Order.OrderType == OrderType).filter(Order.PayStatus == PayStatus).all()
    subdata_list = []
    for i in subdata:
        subdata_list.append(i[0])    
    (data,row_count,page_count,page_no) = database.query_more(subdata,order_by,page_no,page_size)
    session.close()
    return (data,subdata_list,row_count,page_count,page_no)
def query_fitnessorder():
    session = database.get_session()
    fitnessorderlist = session.query(Order).all()
    session.close()
    fitnessorder_list = []
    for i in fitnessorderlist:
        Price =i.Price
        Price = str(Price)
        fitnessorder_list.append({'OrderId':i.OrderId,'OrderName':i.OrderName,'OrderType':i.OrderType,'Amount':i.Amount,'Price':Price,'BuyName':i.BuyName,'BuyerName':i.BuyerName,'Comment':i.Comment})   
    return fitnessorder_list

def search_fitnessorder(searchName):
    session = database.get_session()
    
#     fitnessorderlist = session.query(Order).filter(Order.BuyerName == searchName).all()
    fitnessorderlist = session.query(Order).filter(Order.BuyerName.like('%' + searchName + '%')).all()
    session.close()
    fitnessorder_list = []
    for i in fitnessorderlist:
        Price =i.Price
        Price = str(Price)
        fitnessorder_list.append({'OrderId':i.OrderId,'OrderName':i.OrderName,'OrderType':i.OrderType,'Amount':i.Amount,'Price':Price,'BuyName':i.BuyName,'BuyerName':i.BuyerName,'Comment':i.Comment})   
    return fitnessorder_list
def delete_fitnessorder(Order_Id):
    session = database.get_session()
    session.query(Order).filter(Order.OrderId == Order_Id).delete()
    session.commit()
    session.close()
    return True
      
# def update_goods(GoodsId,Name,Price,DefaultRebate=100,updater):
#     session = database.get_session()
#     session.query(Goods).filter(Goods.GoodsId == GoodsId).update( {'Name':Name.strip(),'Price':Price,'Modifier':updater,
#                                                                    'DefaultRebate':int(DefaultRebate),'LastUpdateDate':datetime.now()})
#     session.commit()
#     session.close()
    
