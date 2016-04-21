# -*- coding: UTF-8 -*- 
import json

from flask import Module,render_template,jsonify, redirect, request,session,g
from src.fitnessconfig import *
from src.services import userservice,employeeservice
from src.models.userprofile import UserStatus



fitnessmanages = Module(__name__)


def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj


@fitnessmanages.route('/fitnessmanages')
def index():
    return render_template('FitnessManages/index.html')

@fitnessmanages.route('/fitnessmanages/getEmployee')
def addNewEmployee():
    name = request.form.get('name')
    phone = request.form.get('phone')
    wchat = request.form.get('wchat')
    birthday = request.form.get('birthday')
    address = request.form.get('address')
    sex = request.form.get('sex')
    employeeservice.employeeAdd(name=name,phone=phone,webChat=wchat,birthday=birthday,address=address,sex=sex)
    return redirect('/fitnessmanages?fullname=&message=#/personnel/management/add')
      

@fitnessmanages.route('/fitnessmanages/getEmployee')
def getEmployee():
    key = request.args.get('searchKey','')
    results=[]
    employees=employeeservice.employeeFuzzyQuery(key)
    for employee in employees:
        results.append({'name':employee.name,'phone':employee.phone,'wchat':employee.wchat,'birthday':employee.birthday,'address':employee.address,'sex':employee.sex})
    

    return json.dumps(results, default=date_handler)
