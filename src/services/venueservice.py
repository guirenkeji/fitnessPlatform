#-*- encoding: utf-8 -*-
'''
Created on 2016年4月18日

@author: Bob Yum
@module: src.services.venueservice
'''
from src.models import database, Venue, Yard
from datetime import datetime


def get(VenueId):
    session = database.get_session()
    venue = session.query(Venue).filter(Venue.VenueId == VenueId).first()
    session.close()
    return venue

def get_yard_by_venue(VenueId):
    session = database.get_session()
    yards = session.query(Yard).filter(Yard.Venue == VenueId).all()
    session.close()
    return yards

def create(Name,PhoneNo,Address,Email,Priority,creator):
    session = database.get_session()
    v = Venue()
    v.Name = Name.strip()
    v.PhoneNo = PhoneNo.strip()
    v.Address = Address.strip()
    v.Email = Email.strip()
    v.Priority = int(Priority)
    v.creator = creator
    session.add(v)
    session.commit()
    session.close()

def create_yard(Venue_id,YardName,Galleryful,Usage,creator):
    session = database.get_session()
    y = Yard()
    y.Venue = int(Venue_id)
    y.YardName = YardName.strip()
    y.Galleryful = int(Galleryful)
    y.Usage = Usage.strip()
    y.creator = creator
    session.add(y)
    session.commit()
    session.close()

def create_yards(Venue_id,datalist,creator):
    session = database.get_session()
    y = Yard()
    for e in datalist:
        y.Venue = int(Venue_id)
        y.YardName = e[0].strip()
        y.Galleryful = int(e[1])
        y.Usage = e[2].strip()
        y.creator = creator
        session.add(y)
    session.commit()
    session.close()
    
def query(page_no,page_size,order_by,current_user):
    session = database.get_session()
    subdata = session.query(Venue).filter(Venue.Creator == current_user).all()
    subdata_list = []
    for i in subdata:
        subdata_list.append(i[0])    
    (data,row_count,page_count,page_no) = database.query_more(subdata,order_by,page_no,page_size)
    session.close()
    return (data,subdata_list,row_count,page_count,page_no)

def delete_yard(YardId):
    session = database.get_session()
    session.query(Yard).filter(Yard.YardId == YardId).delete()
    session.commit()
    session.close()

def delete(VenueId):
    session = database.get_session()
    #先删除所属场地
    session.query(Yard).filter(Yard.Venue == VenueId).delete(synchronize_session=False)
    session.commit() # or session.expire_all()
    #再删除场馆
    session.query(Venue).filter(Venue.VenueId == VenueId).delete()
    session.commit()
    session.close()

def update(VenueId,Name,PhoneNo,Address,Email,Priority,updater):
    session = database.get_session()
    session.query(Venue).filter(Venue.VenueId == VenueId).update({'Name':Name.strip(),'PhoneNo':PhoneNo,
                                                                      'Address':Address,'Email':Email,'Priority':Priority,
                                                                      'Modifier':updater,'LastUpdateDate':datetime.now()})
    session.commit()
    session.close()    
    
def update_yard(YardId,YardName,Galleryful,Usage,updater):
    session = database.get_session()
    session.query(Yard).filter(Yard.YardId == YardId).update({'YardName':YardName.strip(),'Galleryful':Galleryful,
                                                                    'Usage':Usage.strip(),'Modifier':updater,
                                                                    'LastUpdateDate':datetime.now()})
    session.commit()
    session.close()
  
def update_yards(VenueId,datalist,updater):
    session = database.get_session()
    for e in datalist:
        session.query(Yard).filter(Yard.YardId == e[0]).update({'YardName':e[1].strip(),'Galleryful':int(e[2]),
                                                                    'Usage':e[3].strip(),'Modifier':updater,
                                                                    'LastUpdateDate':datetime.now()})
    session.commit()
    session.close()    