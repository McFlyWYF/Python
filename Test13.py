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


#collections,集合模块
#namedtuple是一个函数，用来创建一个自定义的tuple对象
from collections import namedtuple
Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print (p.x)
print (p.y)
#Point对象是tuple的一种子类

#namedtuple('名称', [属性list])
Cricle = namedtuple('Cricle',['x','y','r'])

#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
from collections import deque
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print (q)

#defaultdict,如果希望key不存在时，返回一个默认值，就可以用defaultdict
from collections import defaultdict
dd = defaultdict(lambda:'N/A')
dd['key1'] = 'abc'
print (dd['key1'])#key1存在
print (dd['key2'])#key2不存在,返回默认值

#OrderedDict,保持key的顺序
from collections import OrderedDict
d = dict([('a',1),('b',2),('c',3)])
print (d)# dict的Key是无序的
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print (od)# OrderedDict的Key是有序的
#OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print (list(od.keys()))
#OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key
from collections import OrderedDict
class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

#Counter计数器
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print (c)