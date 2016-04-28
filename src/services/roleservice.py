'''
Created on Apr 24, 2016

@author: shenb2
'''

from src.models.role import Role,Permission
from src.models import database
 

def createRole(roles):
    """
    Create Role
    """

    seesion=database.get_session()
    for r in roles:
        
        querys=seesion.query(Role)
        role = querys.filter_by(name=r).first()
        if role is None:
            role = Role(name=r)
        role.permissions = roles[r][0]
        seesion.add(role)
        seesion.commit()
    seesion.close()
    
def createRoleAdd(rolename):
    r = Role()
    seesion=database.get_session()
    r.name = rolename.strip()

    seesion.add(r)

    seesion.commit()
    seesion.close()
       
def query_role():
    
    session = database.get_session()

    rolelist = session.query(Role).all()
    session.close()
    return rolelist    
def varifyPermission(requiredPerm,roleID):
    seesion=database.get_session()
    querys=seesion.query(Role)
    role = querys.filter_by(id=roleID).first()
    return role.permissions & requiredPerm


if __name__ == '__main__':
    roles = {
        'Manager': (Permission.CROSS_SITE | Permission.ACCOUNTING_WRITE | Permission.ACCOUNTING_READ | Permission.EMPLOYEE_READ | Permission.EMPLOYEE_WRITE | Permission.MEMBER_WRITE | Permission.EMPLOYEE_READ | Permission.SELF_READ | Permission.SELF_WRITE),
        'Shopkeeper': (Permission.ACCOUNTING_WRITE | Permission.ACCOUNTING_READ | Permission.EMPLOYEE_READ | Permission.EMPLOYEE_WRITE | Permission.MEMBER_WRITE | Permission.EMPLOYEE_READ | Permission.SELF_READ | Permission.SELF_WRITE),
        'Coach':(Permission.SELF_READ | Permission.SELF_WRITE),
        'Receptionist':(Permission.MEMBER_WRITE | Permission.EMPLOYEE_READ | Permission.SELF_READ | Permission.SELF_WRITE),
        'Memer': (Permission.SELF_READ | Permission.SELF_WRITE),
        'Other': (Permission.NO_PERMISSION)
    
    } 
    createRole(roles)
    
    print varifyPermission(Permission.EMPLOYEE_READ,1) 