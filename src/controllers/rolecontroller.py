# -*- coding: UTF-8 -*- 
from flask import Module,render_template,redirect,request,session,jsonify,g
from src.services import roleservice
from src.controllers.filters import login_filter

role = Module(__name__)
role.before_request(login_filter)

roleName={ 
    u"用户管理" : 0x01,
    u"课程管理" : 0x02,
    u"商品添加" : 0x04,
    u"商品查询" : 0x08
    }

@role.route('/role/permissionQury',methods=['POST'])
def queryPermission():
    key=request.json.get('id',"")
    data= []
    roleName.keys()
    for item in roleName.keys():
        role={"right":roleName[item],"wrong":0,"name":item}
        if key != "":
            if roleservice.varifyPermission(roleName[item], key):
                role['checked']=1
            else:
                role['checked']=-1
        data.append(role)
    return jsonify(got=True,data=data)

@role.route('/role/add',methods=['POST'])
def createRole():
    roleservice.addRole(request.json['rolename'],request.json['taozhang'],request.json['comments'],permissions=request.json['permissions'])
    return jsonify(created=True)

@role.route('/role/update',methods=['POST'])
def updateRole():
    roleservice.updateRole(request.json['id'],request.json['rolename'],request.json['taozhang'],request.json['comments'],permissions=request.json['permissions'])
    return jsonify(updated=True)

@role.route('/role/delete',methods=['POST'])
def deleteRole():
    roleservice.roleDeleteByID(request.json['roleID'])
    return jsonify(deleted=True)

@role.route('/role/query',methods=['POST'])
def queryRole():
    key=request.json.get('searchName',"")
    lists = roleservice.query_role(key)
    rolelist = []
    for i in lists:
        perms=[]
        for item in roleName.keys():
            key=i.id
            if roleservice.varifyPermission(roleName[item], key):
                perms.append(item)
        rolelist.append({'id':i.id,'rolename':i.name,'permission':" ".join(perms),'taozhang':i.taozhang})
    return jsonify(got=True,data=rolelist)

@role.route('/role/search',methods=['POST'])
def queryRoleKey():
    key=request.json.get('searchKey',"")
    lists=[]
    if key in roleName.keys():
        print key
        print roleName[key]
        lists = roleservice.query_role(permission=roleName[key])
    else:
        lists = roleservice.query_role(name=key)
        
    rolelist = []
    for i in lists:
        perms=[]
        for item in roleName.keys():
            key=i.id
            if roleservice.varifyPermission(roleName[item], key):
                perms.append(item)
        rolelist.append({'id':i.id,'rolename':i.name,'permission':" ".join(perms),'taozhang':i.taozhang})
    return jsonify(got=True,data=rolelist)

@role.route('/role/get',methods=['POST'])
def getRole():
    key=request.json.get('id',"")
    i = roleservice.roleGetByID(key)
    role={'id':i.id,'rolename':i.name,'permissions':i.permissions,'taozhang':i.taozhang,'comments':i.comments}
    return jsonify(got=True,data=role)

