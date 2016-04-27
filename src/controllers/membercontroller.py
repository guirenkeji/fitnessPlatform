# -*- coding: UTF-8 -*- 
import json
import datetime
from flask import Module,render_template,jsonify, redirect, request,session,g
from src.fitnessconfig import *
from src.services import userservice,employeeservice,memberservice
from src.models.userprofile import UserStatus

memberManages = Module(__name__)


def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

@memberManages.route('/fitnessmanages/addMember',methods=["POST"])
def addNewMember():
    
    addOne= request.get_json()
    print "***"*20
    import pprint
    pprint.pprint(addOne)
    name = addOne.get('name')
    comments=addOne.get('comments',None)
    phone = addOne.get('phone')
    wchat = addOne.get('wchat',None)
    birthday = addOne.get('birthday',None)
    if not birthday is None:
        birthday=datetime.datetime.strptime(birthday, '%m/%d/%Y').date() 
    address = addOne.get('address',None)
    memberservice.memberAdd(name=name,phone=phone,webChat=wchat,birthday=birthday,address=address,comments=comments)
    return jsonify(created=True)

@memberManages.route('/fitnessmanages/modifyMember',methods=["GET"])
def modifyMember():
    argDict=request.args.to_dict()
    memberservice.memberModify(argDict.pop('id'),**argDict)
    
    return redirect('/fitnessmanages?fullname=&message=#/personnel/management/add')    


@memberManages.route('/fitnessmanages/searchMember',methods=["POST"])
def searchMember():
    results=[]
    
    members=memberservice.memberFuzzyQuery(request.json['searchKey'],offset=request.json['PageNo'])
    for member in members:
        coach=employeeservice.employeeGetByID(member.coach_id)
        if coach is None:
            coach=''
        else:
            coach = coach.name
        results.append({'id':member.id,'name':member.name,'phone':member.phone,'coach_name':coach,'type':member.type,'status':'ready'})
    
    return jsonify(data=results,row_count=10,page_count=1,page_no=request.json['PageNo'])

@memberManages.route('/fitnessmanages/getMember',methods=["POST"])
def getMemberByID():
    eid = request.json['id']
    member=memberservice.memberGetByID(eid)
    info={}
    for key in member.__dict__:
        if not key.startswith("_"):
            info[key]=member.__dict__[key]
                

    return jsonify(data=info, default=date_handler)
