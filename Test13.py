#常用内建模块
# datetime,处理当前日期和时间的标准库
from datetime import datetime
now = datetime.now()#获取当前datetime
print (now)
print (type(now))
#获取指定日期和时间
from datetime import datetime
dt = datetime(2015,4,19,12,20)
print (dt)
#datetime转timestamp
#timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
#对应的北京时间是timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00

#把datetime类型转换成timestamp调用timestamp()方法
from datetime import datetime
dt = datetime(2015,4,19,12,20)
print (dt.timestamp())

#把timestamp类型转换成datetime调用fromtimestamp()方法
from datetime import datetime
t = 1429417200.5
print (datetime.fromtimestamp(t))

#timestamp也可以直接被转换到UTC标准时区的时间
from datetime import datetime
t = 1429417200.0
print(datetime.fromtimestamp(t)) # 本地时间
print(datetime.utcfromtimestamp(t)) # UTC时间

#str转换为datetime,转换方法是通过datetime.strptime()实现
from datetime import datetime
cday = datetime.strptime('2015-6-1 18:19:59','%Y-%m-%d %H:%M:%S')
print (cday)

#datetime转换为str,转换方法是通过strftime()实现的
from datetime import datetime
now = datetime.now()
print (now.strftime('%a,%b %d %H:%M'))

#datetime加减，加减可以直接用+和-运算符，不过需要导入timedelta这个类
from datetime import datetime,timedelta
now = datetime.now()
print (now)
print (now + timedelta(hours=10))
print (now - timedelta(days=1))
print (now - timedelta(days=1,hours=12))

#本地时间转换为UTC时间,UTC时间指UTC+0:00时区的时间。
from datetime import datetime, timedelta, timezone
tz_utc_8 = timezone(timedelta(hours=8))#创建时区utc+8
now = datetime.now()
print (now)
dt = now.replace(tzinfo = tz_utc_8)#强制设置为UTC+8:00
print (dt)

#时区转换
# 拿到UTC时间，并强制设置时区为UTC+0:00
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print (utc_dt)
# astimezone()将转换时区为北京时间
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print (bj_dt)
# astimezone()将转换时区为东京时间
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print (tokyo_dt)
#任意时区之间相互转换
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print (tokyo_dt2)