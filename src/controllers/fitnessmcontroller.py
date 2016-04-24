# -*- coding: UTF-8 -*- 
import json

from flask import Module,render_template,jsonify, redirect, request,session,g
from src.fitnessconfig import *
from src.services import userservice,employeeservice,memberservice
from src.models.userprofile import UserStatus

fitnessmanages = Module(__name__)


def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

@fitnessmanages.route('/fitnessmanages')
def index():
    return render_template('FitnessManages/index.html')

@fitnessmanages.route('/fitnessmanages/addEmployee',methods=["POST"])
def addNewEmployee():
    
    name = request.form.get('name')
    phone = request.form.get('phone')
    wchat = request.form.get('wchat',None)
    birthday = request.form.get('birthday',None)
    address = request.form.get('address',None)
    sex = request.form.get('sex')
    employeeservice.employeeAdd(name=name,phone=phone,webChat=wchat,birthday=birthday,address=address,sex=sex)
    return redirect('/fitnessmanages?fullname=&message=#/personnel/management/add')

@fitnessmanages.route('/fitnessmanages/addMember',methods=["POST"])
def addNewMember():
    
    name = request.form.get('name')
    phone = request.form.get('phone')
    wchat = request.form.get('wchat',None)
    birthday = request.form.get('birthday',None)
    address = request.form.get('address',None)
    memberservice.memberAdd(name=name,phone=phone,webChat=wchat,birthday=birthday,address=address)
    return redirect('/fitnessmanages?fullname=&message=#/personnel/management/add')

@fitnessmanages.route('/fitnessmanages/modifyEmployee',methods=["GET"])
def modifyEmployee():
    argDict=request.args.to_dict()
    employeeservice.employeeModify(argDict.pop('id'),**argDict)
    
    return redirect('/fitnessmanages?fullname=&message=#/personnel/management/add')  

@fitnessmanages.route('/fitnessmanages/modifyMember',methods=["GET"])
def modifyMember():
    argDict=request.args.to_dict()
    memberservice.memberModify(argDict.pop('id'),**argDict)
    
    return redirect('/fitnessmanages?fullname=&message=#/personnel/management/add')    

@fitnessmanages.route('/fitnessmanages/searchEmployee')
def searchEmployee():
    key = request.args.get('searchKey','')
    results=[]
    employees=employeeservice.employeeFuzzyQuery(key)
    for employee in employees:
        results.append({'id':employee.id,'name':employee.name,'phone':employee.phone,'wchat':employee.wchat,'birthday':employee.birthday,'address':employee.address,'sex':employee.sex})
    

    return json.dumps(results, default=date_handler)

@fitnessmanages.route('/fitnessmanages/searchMember')
def searchMember():
    key = request.args.get('searchKey','')
    results=[]
    members=memberservice.memberFuzzyQuery(key)
    for member in members:
        
        results.append({'id':member.id,'name':member.name,'phone':member.phone,'coach_name':employeeservice.employeeGetByID(member.coach_id).name,'type':member.type})
    

    return json.dumps(results, default=date_handler)

@fitnessmanages.route('/fitnessmanages/getEmployee')
def getEmployeeByID():
    eid = request.args.get('id')
    employ=employeeservice.employeeGetByID(eid)
    info={}
    for key in employ.__dict__:
        if not key.startswith("_"):
            info[key]=employ.__dict__[key]
                

    return json.dumps(info, default=date_handler)

@fitnessmanages.route('/fitnessmanages/getMember')
def getMemberByID():
    eid = request.args.get('id')
    member=memberservice.memberGetByID(eid)
    info={}
    for key in member.__dict__:
        if not key.startswith("_"):
            info[key]=member.__dict__[key]
                

    return json.dumps(info, default=date_handler)
