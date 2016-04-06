# -*- coding: UTF-8 -*- 

from src import create_fitnessPlatform_app
from src.fitnessconfig import *

app = create_fitnessPlatform_app()

if __name__ == '__main__':
    app.debug = True
    app.run(host= HOST,port=PORT)
