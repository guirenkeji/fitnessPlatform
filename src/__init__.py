# -*- coding: UTF-8 -*- 

from flask import Flask
from src.controllers import *

def create_fitnessPlatform_app():
    app = Flask(__name__)
    app.jinja_env.variable_start_string = '(('
    app.jinja_env.variable_end_string = '))'
    app.config.from_pyfile('fitnessconfig.py')
    app.register_module(home)
    app.register_module(user)
    app.register_module(fitnessmanages)
    app.register_module(course)
    return app