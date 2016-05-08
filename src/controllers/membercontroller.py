# -*- coding: UTF-8 -*- 
import json
import datetime
from flask import Module,render_template,jsonify, redirect, request,session,g
from src.fitnessconfig import *
from src.services import userservice,employeeservice,memberservice,roleservice
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
    role = addOne.get('role',None)
    birthday = addOne.get('birthday',None)
    sex = addOne.get('sex',None)
    coach_id = addOne.get('coach',None)
    if not birthday is None:
        birthday=datetime.datetime.strptime(birthday, '%m/%d/%Y').date() 
    address = addOne.get('address',None)
    if memberid != '':
        memberservice.memberAdd(id=memberid,name=name,phone=phone,webChat=wchat,birthday=birthday,address=address,comments=comments,coach_id=coach_id,sex=sex,role=role)
    else:
        memberservice.memberAdd(name=name,phone=phone,webChat=wchat,birthday=birthday,address=address,comments=comments,coach_id=coach_id,sex=sex,role=role)
    return jsonify(created=True)

@memberManages.route('/fitnessmanages/deleteMember',methods=["POST"])
def deleteMember():
    memberservice.memberDeleteByID(request.json['id'])
    
    return jsonify(deleted=True)

@memberManages.route('/fitnessmanages/modifyMember',methods=["POST"])
def modifyMember():
    argDict=request.json
    roleItem=argDict['role']
    if type(roleItem)==dict:
        argDict['role']=argDict['role']["id"]
    memberservice.memberModify(argDict.pop('id'),**argDict)
    
    return jsonify(modified=True)    


@memberManages.route('/fitnessmanages/searchMember',methods=["POST"])
def searchMember():
    results=[]
    
    pageNo = request.json['PageNo']
    if pageNo >0:
        pageNo -=1
    
    members=memberservice.memberFuzzyQuery(request.json['searchKey'],offset=pageNo)
    roleName=''
    
    for member in members:
        roleName=''
        coach=employeeservice.employeeGetByID(member.coach_id)
        if coach is None:
            coach='宗教练'
        else:
            coach = coach.name
        if member.role:
            roleName=roleservice.getNameByID(member.role)
        results.append({'id':member.id,'card':'%05d'%(member.id),'name':member.name,'phone':member.phone,'coach_name':coach,'role':roleName,'status':'ready'})
    
    return jsonify(got=True,data=results,row_count=10,page_count=1,page_no=pageNo)

@memberManages.route('/fitnessmanages/getMember',methods=["POST"])
def getMemberByID():
    eid = request.json['id']
    member=memberservice.memberGetByID(eid) 
    info={}
    for key in member.__dict__:
        if not key.startswith("_"):
            if key == "birthday":
                if member.birthday:
                    info[key]=member.birthday.strftime('%m/%d/%Y')
                else:
                    info[key]=''
            else:
                info[key]=member.__dict__[key]
                

    return jsonify(got=True,data=info)
