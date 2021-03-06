# -*- coding: UTF-8 -*- 
import json

from flask import Module,render_template,jsonify, redirect, request,session,g
from src.fitnessconfig import *
from src.services import userservice,employeeservice,memberservice,orderservice
from src.models.userprofile import UserStatus

fitnessorder = Module(__name__)

@fitnessorder.route('/order/fitnessorder/add',methods=['POST'])
def fitnessOrderAdd():
    OrderName = request.json['OrderName']
#     OrderType = request.json['OrderType']
    OrderType = u"课程"
    Amount = request.json['courseAmount']
    Price = request.json['Price']
    BuyName = u"会员"
#     BuyName = request.json['BuyName']
    BuyerName = request.json['BuyerName']
    Comment = request.json['Comment']
    fitnessorderlist = orderservice.create_fitnessorder(OrderName,OrderType, Price,Amount, BuyName, BuyerName, Comment)
#     password = request.json['Password']
    return jsonify(created=True,data = fitnessorderlist)
@fitnessorder.route('/order/fitnessorder/query',methods=['POST'])
def fitnessOrderQuery():
    PageNo = request.json['PageNo']
    fitnessorderlist = orderservice.query_fitnessorder()
    return jsonify(created=True,data = fitnessorderlist)
@fitnessorder.route('/order/fitnessorder/search',methods=['POST'])
def fitnessOrderSearch():
    searchName = request.json['searchname']
    fitnessorderlist2 = orderservice.search_fitnessorder(searchName)
    return jsonify(created=True,data = fitnessorderlist2)
@fitnessorder.route('/order/fitnessorder/delete',methods=['POST'])
def fitnessOrderDelete():
    OrderId = request.json['OrderId']
    fitnessorderlist = orderservice.delete_fitnessorder(OrderId)
    return jsonify(deleted=True)