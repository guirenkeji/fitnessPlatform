'''
Created on Apr 17, 2016

@author: Bruce
'''
from src.models.database import get_session
from src.models.users.models import Employee,Member
import datetime

def memberQuery(name=None,phone=None,webChat=None,coachID=None,offset=0,limit=10):
    """
    Query employee by name,phone,wehchat. it could be used for page when using offset,limit. Default is return first 10
    """
    seesion=get_session()
    querys=seesion.query(Member)
    if name is not None:
        querys=querys.filter(Member.name.like("%"+name+"%"))
    if phone is not None:
        querys=querys.filter(Member.phone.like(phone+"%"))
    if webChat is not None:
        querys=querys.filter(Member.wchat.like("%"+webChat+"%"))
    if coachID is not None:
        querys=querys.filter(Member.coach_id==coachID)
        
    querys=querys.offset(offset)  
    querys=querys.limit(limit)
    return querys.all()

def memberAdd(name,phone,webChat=None,birthday=None,address=None,expenses_not_quota_password="changeme",coarch=None,**args):
    """
    Add Employee, the default password is 'changeme'. At the first login, we need to force change password
    """

    member=Member()
    member.name=name
    member.phone=phone
    member.password=expenses_not_quota_password
    if not webChat is None:
        member.phone=webChat
    if not birthday is None:
        member.phone=birthday
    if not address is None:
        member.phone=address
    
    for item in args:
        if hasattr(member, item):
            member=args[item]
        else:
            raise "Member Didn't have this property: " + item

if __name__ == '__main__':
    pass