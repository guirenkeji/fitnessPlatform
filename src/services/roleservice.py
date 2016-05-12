'''
Created on Apr 24, 2016

@author: Bruce
'''

from src.models.role import Role,Permission
from src.models import database
 
def roleDeleteByID(roleID):
    """
    Query member by name,phone,wehchat. it could be used for page when using offset,limit. Default is return first 10
    """
    seesion=database.get_session()
    querys=seesion.query(Role).filter(Role.id==roleID)
    role=querys.first()
    
    seesion.delete(role)
    seesion.commit()
    seesion.close()
    
def roleGetByID(roleID):
    """
    Query member by name,phone,wehchat. it could be used for page when using offset,limit. Default is return first 10
    """
    seesion=database.get_session()
    querys=seesion.query(Role).filter(Role.id==roleID)
    role=querys.first()
    seesion.close()
    return role


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
    
def addRole(rolename,taozhang,comments,permissions=0):
    
    r = Role()
    r.name = rolename.strip()
    r.taozhang=taozhang
    r.comments=comments
    r.permissions=permissions
    seesion=database.get_session()
    seesion.add(r)

    seesion.commit()
    seesion.close()

def updateRole(roleid,rolename,taozhang,comments,permissions=0):
    
    r = roleGetByID(roleid)
    r.name = rolename.strip()
    r.taozhang=taozhang
    r.comments=comments
    r.permissions=permissions
    seesion=database.get_session()
    seesion.add(r)

    seesion.commit()
    seesion.close()
       
def query_role(name='',permission=-1):
    
    session = database.get_session()
    querys=session.query(Role)
    if name !='':
        querys=querys.filter(Role.name.like("%"+name+"%"))
    if permission > 0 :
        querys=querys.filter(Role.permissions.op('&')(permission) > 0)
    rolelist = querys.all()
    session.close()
    return rolelist
 
def getNameByID(roleId):
    session = database.get_session()
    querys=session.query(Role)
    role = querys.filter_by(id=roleId).first()
    session.close()
    return role.name

def getIDByName(roleName):
    session = database.get_session()
    querys=session.query(Role)
    role = querys.filter_by(name=roleName).first()
    session.close()
    return role.id
   
def varifyPermission(requiredPerm,roleID):
    seesion=database.get_session()
    querys=seesion.query(Role)
    role = querys.filter_by(id=roleID).first()
    seesion.close()
    return role.permissions & requiredPerm


if __name__ == '__main__':
    pass
#     roles = {
#         'Manager': (Permission.CROSS_SITE | Permission.ACCOUNTING_WRITE | Permission.ACCOUNTING_READ | Permission.EMPLOYEE_READ | Permission.EMPLOYEE_WRITE | Permission.MEMBER_WRITE | Permission.EMPLOYEE_READ | Permission.SELF_READ | Permission.SELF_WRITE),
#         'Shopkeeper': (Permission.ACCOUNTING_WRITE | Permission.ACCOUNTING_READ | Permission.EMPLOYEE_READ | Permission.EMPLOYEE_WRITE | Permission.MEMBER_WRITE | Permission.EMPLOYEE_READ | Permission.SELF_READ | Permission.SELF_WRITE),
#         'Coach':(Permission.SELF_READ | Permission.SELF_WRITE),
#         'Receptionist':(Permission.MEMBER_WRITE | Permission.EMPLOYEE_READ | Permission.SELF_READ | Permission.SELF_WRITE),
#         'Memer': (Permission.SELF_READ | Permission.SELF_WRITE),
#         'Other': (Permission.NO_PERMISSION)
#     
#     } 
#     createRole(roles)
#     
#     print varifyPermission(Permission.EMPLOYEE_READ,1) 