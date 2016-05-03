# -*- coding: UTF-8 -*- 
from flask import Module,render_template,redirect,request,session,jsonify,g
from src.services import roleservice
from src.controllers.filters import login_filter

role = Module(__name__)
role.before_request(login_filter)

roleName={ "无权限" :0x00,
    "读取本人信息" : 0x01 ,
    "修改本人信息" : 0x02,
    "会员信息读取" : 0x04,
    "会员信息修改" : 0x08,
    "员工信息读取" : 0x10,
    "员工信息修改" : 0x20,
    "套帐信息读取" : 0x40,
    "套帐信息修改" : 0x80,
    "跨套帐" : 0x100}

@role.route('/role/permissionQury',methods=['POST'])
def queryPermission():
    data= roleName.keys()
    return jsonify(created=True,data=data)

@role.route('/role/add',methods=['POST'])
def createRole():
    roleservice.createRoleAdd(request.json['rolename'],request.json['taozhang'],request.json['comments'])
    return jsonify(created=True)

@role.route('/role/delete',methods=['POST'])
def deleteRole():
    roleservice.roleDeleteByID(request.json['roleID'])
    return jsonify(deleted=True)

@role.route('/role/query',methods=['POST'])
def queryRole():
    PageNo=request.json['PageNo']
    list = roleservice.query_role()
    rolelist = []
    for i in list:
        rolelist.append({'id':i.id,'rolename':i.name,'permission':'管理员','taozhang':i.taozhang})
    return jsonify(data=rolelist)

