#-*- encoding: utf-8 -*-
'''
Created on 2016年4月18日

@author: Bob Yum
@module: src.controllers.coursecontroller
'''
from flask import Module,render_template,jsonify, request,g,session,redirect
from src.services import courseservice
from src.fitnessconfig import *
from src.controllers.filters import login_filter

course = Module(__name__)
#course.before_request(login_filter)

PAGESIZE = 20

@course.route('/fitnessmanages/Course')
def index():
    return render_template('teamCourses/add.html')

@course.route('/courses/private/management/add',methods=['POST'])
def privateCoursesAdd():
    courseservice.create_course('b',request.json['fullname'],request.json['data-class-time'],10,200,'',request.json['message'],g.user_id)
    return jsonify(created=True)

@course.route('/courses/team/management/add',methods=['POST'])
def teamCoursesAdd():
    courseservice.create_course('a',request.json['fullname'],request.json['dataclasstime'],10,200,'',request.json['message'],1)
    return jsonify(created=True)

@course.route('/courses/private/query',methods=['POST'])
def privateCoursesManagement():
    page_no = request.json['PageNo']
    (data,subdata_list,row_count,page_count,page_no) = courseservice.query(page_no,PAGESIZE,'LastUpdateDate',1,'b')
    courses = []
    for p in data.all():
        courses.append({'Name':p.Name,'Duration':p.Duration,'Amount':p.Amount,'Coach':'Test','CreateDate':p.CreateDate.isoformat()})
    return jsonify(data=courses,row_count=row_count,page_count=page_count,page_no=page_no)

@course.route('/courses/team/query',methods=['POST'])
def teamCoursesManagement():
    page_no = request.json['PageNo']
    (data,subdata_list,row_count,page_count,page_no) = courseservice.query(page_no,PAGESIZE,'LastUpdateDate',1)
    courses = []
    for p in data.all():
        courses.append({'Name':p.Name,'Duration':p.Duration,'Amount':p.Amount,'Coach':'Test','CreateDate':p.CreateDate.isoformat()})
    return jsonify(data=courses,row_count=row_count,page_count=page_count,page_no=page_no)

@course.route('/fitnessmanages/Course/Delete',methods=['POST'])
def delete_course():
    CourseId = request.json['CourseId']
    courseservice.delete_course(CourseId)
    return jsonify(deleted=True)

@course.route('/fitnessmanages/Course/Update',methods=['POST'])
def update_course():
    CourseId = request.json['CourseId']
    Name = request.json['Name']
    Duration = request.json['Duration']
    Amount = request.json['Amount']
    Coach = request.json['Coach']
    HourFee = request.json['HourFee']
    Comment = request.json['Comment']
    Description = request.json['Description']
    Creator = g.user_id
    courseservice.update_course(CourseId,Name,Duration,Amount,Coach,HourFee,Comment,Description,Creator)
    return jsonify(updated=True)

