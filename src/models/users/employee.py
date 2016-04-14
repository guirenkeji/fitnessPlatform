'''
Created on Apr 14, 2016

@author: Bruce
'''
from src.models.database import get_session
from src.models.users.models import Employee


def employeeQuery(name=None,phone=None,webChat=None):
    seesion=get_session()
    querys=seesion.query(Employee)
    if name is not None:
        querys=querys.filter(Employee.name==name)
    if phone is not None:
        querys=querys.filter(Employee.phone==phone)
    if webChat is not None:
        querys=querys.filter(Employee.name==webChat)
    return querys.all()
    
    
    
    
        