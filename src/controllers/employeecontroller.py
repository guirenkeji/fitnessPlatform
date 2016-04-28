# -*- coding: UTF-8 -*- 
import json

from flask import Module,render_template,jsonify, redirect, request,session,g
from src.fitnessconfig import *
from src.services import userservice,employeeservice,memberservice
from src.models.userprofile import UserStatus
import datetime
employeemanages = Module(__name__)


def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

@employeemanages.route('/fitnessmanages/addEmployee',methods=["POST"])
def addNewEmployee():
      
    addOne= request.get_json()
    
    name = addOne.get('name')
    comments=addOne.get('comments',None)
    phone = addOne.get('phone')
    wchat = addOne.get('wchat',None)
    birthday = addOne.get('birthday',None)
    if not birthday is None:
        birthday=datetime.datetime.strptime(birthday, '%m/%d/%Y').date() 
    address = addOne.get('address',None)
    sex = addOne.get('sex','man')
    employeeservice.employeeAdd(name=name,phone=phone,webChat=wchat,birthday=birthday,address=address,sex=sex)
    return jsonify(created=True)


@employeemanages.route('/fitnessmanages/modifyEmployee',methods=["GET"])
def modifyEmployee():
    argDict=request.args.to_dict()
    employeeservice.employeeModify(argDict.pop('id'),**argDict)
    
    return redirect('/fitnessmanages?fullname=&message=#/personnel/management/add')  


@employeemanages.route('/fitnessmanages/searchEmployee',methods=["POST"])
def searchEmployee():
    key = request.json['searchKey']
    results=[]
    employees=employeeservice.employeeFuzzyQuery(key)
    for employee in employees:
        bd =employee.birthday
        if not bd is None:
            bd=bd.strftime('%m/%d/%Y')
        if employee.sex == 'man':
            sex='男'
        else:
            sex='女'
        results.append({'id':employee.id,'name':employee.name,'phone':employee.phone,'wchat':employee.wchat,'birthday':bd,'address':employee.address,'sex':sex,'taozhang':'CN'})
    

    return jsonify(data=results,row_count=len(employees),page_count=1,page_no=request.json['PageNo'])


@employeemanages.route('/fitnessmanages/deleteEmployee',methods=["POST"])
def deleteEmployeeByID():
    employeeservice.employeeDeleteByID(request.json['id'])
    
    return jsonify(deleted=True)

@employeemanages.route('/fitnessmanages/getEmployee')
def getEmployeeByID():
    eid = request.args.get('id')
    employ=employeeservice.employeeGetByID(eid)
    info={}
    for key in employ.__dict__:
        if not key.startswith("_"):
            info[key]=employ.__dict__[key]
                

    return json.dumps(info, default=date_handler)

