#-*- encoding: utf-8 -*-
'''
Created on 2016年4月18日

@author: Bob Yum
@module: src.services.courseservice
'''
from src.models import database,Course,Plan,Member,Yard
from datetime import datetime

def get_course(CourseId):
    session = database.get_session()
    course = session.query(Course).filter(Course.CourseId == CourseId).first()
    session.close()
    return course

def get_plan(PlanId):
    session = database.get_session()
    plan = session.query(Plan).filter(Plan.PlanId == PlanId).first()
    session.close()
    return plan

def get_course_by_ctype(ctype,creator):
    session = database.get_session()
    courses = session.query(Course).filter(Course.Creator == creator).filter(Course.CType == ctype).all()
    session.close()
    return courses

def get_plan_by_ptype(ptype,creator):
    session = database.get_session()
    plans = session.query(Plan).filter(Plan.Creator == creator).filter(Plan.PType == ptype).all()
    session.close()
    return plans

def create_course(CourseType,Name,Duration,Amount,HourFee,Comment,Description,creator,Coach_id=None):
    session = database.get_session()
    p = Course()
    p.CType = CourseType.strip()
    p.Name = Name.strip()
    p.Duration = int(Duration)
    p.Amount = int(Amount)
    if Coach_id:
        m = Member()
        m.UserId = Coach_id
        p.Coach.append(m)
    p.HourFee = int(HourFee)
    p.Comment = Comment.strip()
    p.Description = Description.strip()
    p.Creator = creator
    p.CreateDate = datetime.now()
    session.add(p)
    session.commit()
    session.close()

def create_plan(PlanType,CourseId,Yardid,BeginDate,EndDate,WorkTime,OffTime,WeekSchedule_list_or_str,creator):
    session = database.get_session()
    p = Plan()
    p.PType = PlanType.strip()
    c = Course()
    c.CourseId = CourseId
    p.Course.append(c)
    y = Yard()
    y.Yardid = Yardid
    p.Yard.append(y)
    p.BeginDate = BeginDate
    p.EndDate = EndDate
    if PlanType.strip() == 'a': #团课
        s = ''
        for e in WeekSchedule_list_or_str:
            s+= '&'.join(e)+'^'
        p.WeekSchedule = s.strip('^')
    elif PlanType.strip() == 'b':  #私教
        p.WorkTime = WorkTime
        p.OffTime = OffTime
        p.WeekSchedule = WeekSchedule_list_or_str
    else:
        pass
    p.Creator = creator
    p.CreateDate = datetime.now()
    session.add(p)
    session.commit()
    session.close()
    
def query(page_no,page_size,order_by,current_user):
    session = database.get_session()
    subdata = session.query(Course).filter(Course.Creator == current_user).all()
    subdata_list = []
    for i in subdata:
        subdata_list.append(i[0])    
    (data,row_count,page_count,page_no) = database.query_more(subdata,order_by,page_no,page_size)
    session.close()
    return (data,subdata_list,row_count,page_count,page_no)

def delete_course(CourseId):
    session = database.get_session()
    #先删除课程安排信息
    session.query(Plan).filter(Plan.Course == [CourseId]).delete(synchronize_session=False)
    session.commit()
    #再删除课程
    session.query(Course).filter(Course.CourseId == CourseId).delete()
    session.commit()
    session.close()

def delete_plan(PlanId):
    session = database.get_session()
    session.query(Plan).filter(Plan.PlanId == PlanId).delete()
    session.commit()
    session.close()
        
def update_course(CourseId,Name,Duration,Amount,Coach_id,HourFee,Comment,Description,updater):
    session = database.get_session()
    updatedict = {'Name':Name.strip(),'Duration':int(Duration),'Amount':int(Amount),'HourFee':int(HourFee),
                  'Comment':Comment.strip(),'Description':Description.strip(),'Modifier':updater,
                  'LastUpdateDate':datetime.now()}
    if Coach_id:
        m = Member()
        m.UserId = Coach_id
        updatedict.update({'Coach':[m]})
    session.query(Course).filter(Course.CourseId == CourseId).update(updatedict)
    session.commit()
    session.close()
    
def update_plan(ptype,CourseId,Yardid,Coach_id,BeginDate,EndDate,WorkTime,OffTime,WeekSchedule_list_or_str,updater):
    session = database.get_session()
    updatedict = {'BeginDate':BeginDate,'EndDate':EndDate,'Modifier':updater,'LastUpdateDate':datetime.now()}
    if CourseId:
        c = Course()
        c.CourseId = CourseId
        updatedict.update({'Course':[c]})
    if Yardid:
        y = Yard()
        y.Yardid = Yardid
        updatedict.update({'Yard':[y]})
    if Coach_id:
        m = Member()
        m.UserId = Coach_id
        updatedict.update({'Coach':[m]})
    if WorkTime:
        updatedict.update({'WorkTime':WorkTime})
    if OffTime:
        updatedict.update({'OffTime':OffTime})
    if WeekSchedule_list_or_str:
        if ptype=='a':
            s = ''
            for e in WeekSchedule_list_or_str:
                s+= '&'.join(e)+'^'
            updatedict.update({'WeekSchedule':s.strip('^')})
        elif ptype=='b':
            updatedict.update({'WeekSchedule':WeekSchedule_list_or_str})
        else:
            pass
    session.query(Course).filter(Course.CourseId == CourseId).update(updatedict)
    session.commit()
    session.close()
    