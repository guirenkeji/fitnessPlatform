'''
Created on Apr 17, 2016

@author: Bruce
'''
from src.models.database import get_session
from src.models.member import Member
import datetime
from sqlalchemy import or_


def memberFuzzyQuery(key,offset=0,limit=10):
    seesion=get_session()
    querys=seesion.query(Member)
    querys=querys.filter(or_(Member.name.like("%"+key+"%"),Member.phone.like("%"+key+"%"),Member.wchat.like("%"+key+"%")))

    
    querys=querys.offset(offset)  
    querys=querys.limit(limit)
    return querys.all()

def memberGetByID(employId):
    """
    Query member by name,phone,wehchat. it could be used for page when using offset,limit. Default is return first 10
    """
    seesion=get_session()
    querys=seesion.query(Member).filter(Member.id==employId)
    member=querys.first()
    seesion.close()
    return member

def memberModify(employId,**args):
    session=get_session()
    
    querys=session.query(Member).filter(Member.id==employId)
    member = querys.first()

    session.add(member)
    for item in args:
        if hasattr(member, item):
            setattr(member, item,args[item])
        else:
            raise "Member Didn't have this property: " + item
    session.commit()
    session.close()

def memberQuery(name=None,phone=None,webChat=None,coachID=None,offset=0,limit=10):
    """
    Query member by name,phone,wehchat. it could be used for page when using offset,limit. Default is return first 10
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

def memberAdd(name,phone,webChat=None,birthday=None,address=None,expenses_not_quota_password="changeme",**args):
    """
    Add Member, the default password is 'changeme'. At the first login, we need to force change password
    """
    session=get_session()
    
    member=Member()
    
    member.name=name
    member.phone=phone
    member.expenses_not_quota_password=expenses_not_quota_password
    if not webChat is None:
        member.webChat=webChat
    if not birthday is None:
        member.phone=birthday
    if not address is None:
        member.phone=address
    
    for item in args:
        if hasattr(Member, item):
            setattr(member,item,args[item])
        else:
            raise  Exception("Member Didn't have this property: " + item)
    session.add(member)
    session.commit()
    session.close()
    

if __name__ == '__main__':
    import sys
    from src.models import database
    from datetime import datetime
    import pprint
    
    i=1
    while i <200:
        print i
         
        memberAdd(name='memebr'+str(i),phone=177+i,webChat="mywebchat"+str(i),birthday=None,address=None,expenses_not_quota_password="changeme",coach_id=i,body_info="Good "+ str(i))
        i +=1
    
    results= memberFuzzyQuery('1')