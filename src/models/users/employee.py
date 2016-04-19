'''
Created on Apr 14, 2016

@author: Bruce
'''
from src.models.database import get_session
from src.models.users.models import Employee,Member
import datetime

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
    employee=Employee()
    employee.name=name
    employee.phone=phone
    employee.password=password
    if not webChat is None:
        employee.phone=webChat
    if not birthday is None:
        employee.phone=birthday
    if not address is None:
        employee.phone=address
        
    for item in args:
        if hasattr(employee, item):
            employee=args[item]
        else:
            raise "Employee Didn't have this property: " + item

    
if __name__ == '__main__':
    import sys
    from src.models import database,UserProfile,UserStatus
    from datetime import datetime
#     database.drop_database()
#     database.create_database()
    session = database.get_session()

    
#     i=0
#     while i <200:
#         print i
#         user1 = Employee()  
#         user1.name = 'bruce'+str(i)
#         user1.phone = u'189'+str(i)
#         user1.wchat = 'test'+str(i)
#         user1.birthday = datetime.now()
#         i=i+1
#         session.add(user1)
#         session.commit()
#     session.close()    
    results= employeeQuery('bruce','189',offset=10,limit=20)
    for item in results:
        print item.birthday
    print dir(Employee)
        