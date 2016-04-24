#-*- encoding: utf-8 -*-
'''
Created on 2016年4月18日

@author: Bob Yum
@module: src.controllers.coursecontroller
'''
from flask import Module,render_template,jsonify, request,g
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
    print request.json
    courseservice.create_course('a',request.json['fullname'],request.json['dataclasstime'],10,200,'',request.json['message'],1)
    return jsonify(created=True)

@course.route('/fitnessmanages/Course/Query',methods=['POST'])
def query():
    page_no = request.json['PageNo']
    class_name = request.json['ClassName']
    checked_list = request.json['CheckedList']
    (data,subdata,row_count,page_count,page_no) = courseservice.query(page_no,PAGESIZE,'LastUpdateDate',g.user_id,class_name)
    projects = []
    for p in data.all():
        if subdata == []:
            isChecked = True if p.ProjectId in checked_list else False
            projects.append({'ProjectId':p.ProjectId,'ProjectName':p.ProjectName,'Introduction':p.Introduction,'CreateDate':p.CreateDate.isoformat(),'LastUpdateDate':p.LastUpdateDate.isoformat(),'Creator':p.UserProfile.Nick,'IsChecked':isChecked})
        else :
            if p.ProjectId in subdata:
                projects.append({'ProjectId':p.ProjectId,'ProjectName':p.ProjectName,'Introduction':p.Introduction,'CreateDate':p.CreateDate.isoformat(),'LastUpdateDate':p.LastUpdateDate.isoformat(),'Creator':p.UserProfile.Nick})
    return jsonify(data=projects,row_count=row_count,page_count=page_count,page_no=page_no)

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

