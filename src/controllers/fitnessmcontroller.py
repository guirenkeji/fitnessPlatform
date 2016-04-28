# -*- coding: UTF-8 -*- 
import json

from flask import Module,render_template,jsonify, redirect, request,session,g
from src.fitnessconfig import *
from src.services import userservice,employeeservice,memberservice
from src.models.userprofile import UserStatus

fitnessmanages = Module(__name__)


@fitnessmanages.route('/fitnessmanages')
def fitnessmanage():
    return render_template('FitnessManages/index.html')
