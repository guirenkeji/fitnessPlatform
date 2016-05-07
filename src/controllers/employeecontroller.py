# -*- coding: UTF-8 -*- 
import json

from flask import Module,render_template,jsonify, redirect, request,session,g
from src.fitnessconfig import *
from src.services import userservice,employeeservice,roleservice
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
    employeeservice.employeeAdd(name=name,phone=phone,webChat=wchat,birthday=birthday,address=address,sex=sex,comments=comments,role=addOne.get('role'))
    return jsonify(created=True)


@employeemanages.route('/fitnessmanages/modifyEmployee',methods=["POST"])
def modifyEmployee():
    argDict=request.json
    if argDict.has_key('birthday'):
        argDict['birthday'] = datetime.datetime.strptime(argDict['birthday'], '%m/%d/%Y').date() 
    employeeservice.employeeModify(argDict.pop('id'),**argDict)
    
    return jsonify(updated=True) 


@employeemanages.route('/fitnessmanages/searchEmployee',methods=["POST"])
def searchEmployee():
    key = request.json['searchKey']
    pageNo = request.json['PageNo']
    if pageNo >0:
        pageNo -=1
    results=[]
    employees=employeeservice.employeeFuzzyQuery(key)
    for employee in employees:
        bd =employee.birthday
        roleName=''
        if not bd is None:
            bd=bd.strftime('%m/%d/%Y')
        if employee.sex == 'man':
            sex='男'
        else:
            sex='女'
        roleName=roleservice.getNameByID(employee.role)
        results.append({'id':employee.id,'name':employee.name,'role':roleName,'phone':employee.phone,'wchat':employee.wchat,'birthday':bd,'address':employee.address,'sex':sex,'taozhang':'CN'})
    

    return jsonify(got=True,data=results,row_count=len(employees),page_count=1,page_no=pageNo)

@employeemanages.route('/fitnessmanages/searchEmployeeByRole',methods=["POST"])
def searchEmployeeByRole():
    key = request.json['searchKey']
    pageNo = request.json['PageNo']
    if pageNo >0:
        pageNo -=1
    results=[]
    employees=employeeservice.employeeQueryByRoleName(key)
    for employee in employees:
        bd =employee.birthday
        roleName=''
        if not bd is None:
            bd=bd.strftime('%m/%d/%Y')
        if employee.sex == 'man':
            sex='男'
        else:
            sex='女'
        roleName=roleservice.getNameByID(employee.role)
        results.append({'id':employee.id,'name':employee.name,'role':roleName,'phone':employee.phone,'wchat':employee.wchat,'birthday':bd,'address':employee.address,'sex':sex,'taozhang':'CN'})
    

    return jsonify(got=True,data=results,row_count=len(employees),page_count=1,page_no=pageNo)

@employeemanages.route('/fitnessmanages/deleteEmployee',methods=["POST"])
def deleteEmployeeByID():
    employeeservice.employeeDeleteByID(request.json['id'])
    
    return jsonify(deleted=True)

@employeemanages.route('/fitnessmanages/getEmployee',methods=["POST"])
def getEmployeeByID():
    eid = request.json['id']
    employ=employeeservice.employeeGetByID(eid)
    info={}
    info['name']=employ.name
    info['birthday']=employ.birthday.strftime('%m/%d/%Y')
    info['sex']=employ.sex
    info['phone']=employ.phone
    info['wchat']=employ.wchat
    info['comments']=employ.comments
    info['role']= employ.role
    info['address']=employ.address
                

    return jsonify(got=True,data=info)

