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
    memberid = addOne.get('memberid','')
    name = addOne.get('name')
    comments=addOne.get('comments',None)
    phone = addOne.get('phone')
    wchat = addOne.get('wchat',None)
    birthday = addOne.get('birthday',None)
    coach_id = addOne.get('coach',None)
    if not birthday is None:
        birthday=datetime.datetime.strptime(birthday, '%m/%d/%Y').date() 
    address = addOne.get('address',None)
    if memberid != '':
        memberservice.memberAdd(id=memberid,name=name,phone=phone,webChat=wchat,birthday=birthday,address=address,comments=comments,coach_id=coach_id)
    else:
        memberservice.memberAdd(name=name,phone=phone,webChat=wchat,birthday=birthday,address=address,comments=comments,coach_id=coach_id)
    return jsonify(created=True)

@memberManages.route('/fitnessmanages/deleteMember',methods=["POST"])
def deleteMember():
    memberservice.memberDeleteByID(request.json['id'])
    
    return jsonify(deleted=True)

@memberManages.route('/fitnessmanages/modifyMember',methods=["GET"])
def modifyMember():
    argDict=request.json
    memberservice.memberModify(argDict.pop('id'),**argDict)
    
    return jsonify(modified=True)    


@memberManages.route('/fitnessmanages/searchMember',methods=["POST"])
def searchMember():
    results=[]
    
    pageNo = request.json['PageNo']
    if pageNo >0:
        pageNo -=1
    
    members=memberservice.memberFuzzyQuery(request.json['searchKey'],offset=pageNo)
    for member in members:
        coach=employeeservice.employeeGetByID(member.coach_id)
        if coach is None:
            coach='宗教练'
        else:
            coach = coach.name
        type= member.type
        if type != 'vip':
            type='普通'
        else:
            type = 'VIP'
        results.append({'id':member.id,'card':'%05d'%(member.id),'name':member.name,'phone':member.phone,'coach_name':coach,'type':type,'status':'ready'})
    
    return jsonify(got=True,data=results,row_count=10,page_count=1,page_no=pageNo)

@memberManages.route('/fitnessmanages/getMember',methods=["POST"])
def getMemberByID():
    eid = request.json['id']
    member=memberservice.memberGetByID(eid) 
    info={}
    for key in member.__dict__:
        if not key.startswith("_"):
            if key == "birthday":
                print 
                info[key]=member.birthday.strftime('%m/%d/%Y')
            else:
                info[key]=member.__dict__[key]
                

    return jsonify(got=True,data=info)
