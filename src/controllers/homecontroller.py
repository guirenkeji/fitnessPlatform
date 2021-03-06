# -*- coding: UTF-8 -*- 

from flask import Module,render_template,jsonify, redirect, request,session,g
from src.fitnessconfig import *
from src.services import userservice,employeeservice
from src.models.userprofile import UserStatus

home = Module(__name__)


@home.route('/')
def index():
    if 'username' in session and not session['username'] == None:
        return redirect('/fitnessmanages')
    return render_template('Login.html',
                           title = u'登陆'
                           )
    return redirect('/fitnessmanages')

@home.route('/Login',methods=['POST'])
def login():
    email = request.json['Email']
    password = request.json['Password']
    user = userservice.get(email)
    if user == None:
        response = jsonify(isDisabled = False,isMatch=False)
        return response

    if not user.password == password:
        response = jsonify(isDisabled = False,isMatch=False)
        return response

    session['userid'] = user.id
    session['username'] = user.name
    response = jsonify(isDisabled=False,isMatch=True)
    return response

@home.route('/Register')
def register():
    return render_template('Register.html',
                           title = u'注册')

@home.route('/Register/Save',methods=['POST'])
def save():
    (exist,userid) = userservice.register(request.json['Email'],request.json['Nick'],request.json['Password'])

    if not exist:
        session['userid'] = userid
        session['username'] = request.json['Email']
    session['isadmin'] = False
    result = {'created' : not exist}
    return jsonify(result)
