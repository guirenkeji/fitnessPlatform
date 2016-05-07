'''
Created on Apr 14, 2016

@author: Bruce
'''
from src.models.database import get_session
from src.models.employee import Employee
from src.models.member import Member
from src.services import roleservice
import datetime
from sqlalchemy import or_


def employeeFuzzyQuery(key,offset=0,limit=10):
    seesion=get_session()
    querys=seesion.query(Employee)
    querys=querys.filter(or_(Employee.name.like("%"+key+"%"),Employee.phone.like("%"+key+"%"),Employee.wchat.like("%"+key+"%")))

    
    querys=querys.offset(offset)  
    querys=querys.limit(limit)
    return querys.all()

def employeeQueryByRoleName(key,offset=0,limit=10):
    seesion=get_session()
    roleID=roleservice.getIDByName(key)
    querys=seesion.query(Employee).filter(Employee.role==roleID)
    
    querys=querys.offset(offset)  
    querys=querys.limit(limit)
    return querys.all()

def employeeGetByID(employId):
    """
    Query employee by name,phone,wehchat. it could be used for page when using offset,limit. Default is return first 10
    """
    seesion=get_session()
    querys=seesion.query(Employee).filter(Employee.id==employId)
    employee=querys.first()
    seesion.close()
    return employee

def employeeDeleteByID(employId):
    """
    Delete employee by id
    """
    seesion=get_session()
    querys=seesion.query(Employee).filter(Employee.id==employId)
    employee=querys.first()
    
    seesion.delete(employee)
    seesion.commit()
    seesion.close()
    return employee

def employeeModify(employId,**args):
    session=get_session()
    
    querys=session.query(Employee).filter(Employee.id==employId)
    employee = querys.first()

    session.add(employee)
    for item in args:
        if hasattr(employee, item):
            setattr(employee, item,args[item])
        else:
            raise "Employee Didn't have this property: " + item
    session.commit()
    session.close()
    
def employeeQuery(name=None,phone=None,webChat=None,offset=0,limit=10):
    """
    Query employee by name,phone,wehchat. it could be used for page when using offset,limit. Default is return first 10
    """
    seesion=get_session()
    querys=seesion.query(Employee)
    if name is not None:
        querys=querys.filter(Employee.name.like("%"+name+"%"))
    if phone is not None:
        querys=querys.filter(Employee.phone.like(phone+"%"))
    if webChat is not None:
        querys=querys.filter(Employee.wchat.like("%"+webChat+"%"))
    querys=querys.offset(offset)  
    querys=querys.limit(limit)
    return querys.all()

def employeeAdd(name,phone,webChat=None,birthday=None,address=None,password="changeme",**args):
    """
    Add Employee, the default password is 'changeme'. At the first login, we need to force change password
    """
    session=get_session()
    
    employee=Employee()
    
    employee.name=name
    employee.phone=phone
    employee.password=password
    if not webChat is None:
        employee.wchat=webChat
    if not birthday is None:
        employee.birthday=birthday
    if not address is None:
        employee.address=address
        
    for item in args:
        if hasattr(Employee, item):
            setattr(employee,item,args[item])
        else:
            raise "Employee Didn't have this property: " + item
    session.add(employee)
    session.commit()
    session.close()

def employeePermissionCheck(employeeID,permission):
    user=employeeGetByID(employeeID)
    return roleservice.varifyPermission(permission,user.Role)
        
if __name__ == '__main__':
    import sys
    from src.models import database,UserProfile,UserStatus
    from datetime import datetime
    import pprint
#     database.drop_database()
#     database.create_database()
    session = database.get_session()

    
    i=0
    while i <200:
        print i
         
        employeeAdd(name='memebr'+str(i),phone=177+i,webChat="mywebchat"+str(i),birthday=None,address=None)
        i +=1

        