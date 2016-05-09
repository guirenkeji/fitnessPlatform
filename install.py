# -*- coding: UTF-8 -*- 

import sys
from src.models import database,UserProfile,UserStatus,Course,Plan,Venue,Yard,UsageStatus,Employee,Member,Role

from datetime import datetime

if '-dropcreate' in sys.argv:
    database.drop_database()
    print(u'删除数据库完成')
# database.drop_database()
database.create_database()
print(u'创建数据库完成')


session = database.get_session()

manage=Role()
manage.name=u"管理员"
session.add(manage)
session.commit()

role=Role()
role.name=u"普通会员"
session.add(role)
session.commit()

role=Role()
role.name=u"VIP会员"
session.add(role)
session.commit()

manage=Role()
manage.name=u"管理员"
session.add(manage)
session.commit()

role=Role()
role.name=u"教练"
session.add(role)
session.commit()


admin = Employee()
admin.name = 'admin'
admin.phone = '1888888888'
admin.password = 'admin'
admin.role=manage.id

session.add(admin)
session.commit()
session.close()


print(u'fitnessPlatform安装完成')
