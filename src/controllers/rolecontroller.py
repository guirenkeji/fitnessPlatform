# -*- coding: UTF-8 -*- 
from flask import Module,render_template,redirect,request,session,jsonify,g
from src.services import roleservice
from src.controllers.filters import login_filter

role = Module(__name__)
role.before_request(login_filter)

@role.route('/role/add',methods=['POST'])
def createRole():
    roleservice.createRoleAdd(request.json['name'])
    return jsonify(created=True,rolename=request.json['name'])
@role.route('/role/query',methods=['POST'])
def queryRole():
    PageNo=request.json['PageNo']
    list = roleservice.query_role()
    rolelist = []
    for i in list:
        rolelist.append({'roleid':i.id,'rolename':i.name})
    return jsonify(data=rolelist)

