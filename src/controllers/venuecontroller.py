#-*- encoding: utf-8 -*-
'''
Created on 2016年4月18日

@author: Bob Yum
@module: src.controllers.venuecontroller
'''
from flask import Module,render_template
from src.controllers.filters import login_filter

venue = Module(__name__)
venue.before_request(login_filter)

@venue.route('/venue')
def index():
    return render_template('venue/index.html')