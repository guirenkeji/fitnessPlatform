# -*- coding: UTF-8 -*- 

from flask import Module,render_template,jsonify, redirect, request,session,g
from src.fitnessconfig import *
from src.services import userservice
from src.models.userprofile import UserStatus

fitnessmanages = Module(__name__)

@fitnessmanages.route('/fitnessmanages')
def index():
    return render_template('FitnessManages/index.html')