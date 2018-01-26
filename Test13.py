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

#base64是一种用64个字符来表示任意二进制数据的方法
import base64
print (base64.b64encode(b'binary\x00string'))
print (base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))

print (base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print (base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print (base64.urlsafe_b64decode('abcd--__'))

#标准的base64
#'abcd' -> 'YWJjZA=='
#自动去掉=
#'abcd' -> 'YWJjZA'


#struct,字节数组＝二进制str,解决bytes和其他二进制数据的转换
#struct的pack函数把任意数据类型变成bytes
import struct
print (struct.pack('>I',10240099))
'''pack的第一个参数是处理指令，'>I'的意思是：
>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
后面的参数个数要和处理指令一致。'''
#unpack把bytes变成相应的数据类型
print (struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))
#I：4字节无符号整数和H：2字节无符号整数。

#hashlib提供了常见的摘要算法，又称哈希算法、散列算法，它通过一个函数，把任意长度的数据转换为一个长度固定的数据串
#摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过。
#摘要算法MD5
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print (md5.hexdigest())
#摘要算法SHA1
import hashlib
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in'.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print (sha1.hexdigest())

#Hmac,带key的哈希值
import hmac
message = b'Hello, world!'
key = b'secret'
h = hmac.new(key,message,digestmod = 'MD5')
print (h.hexdigest())

#itertools，操作迭代对象的函数
'''
import itertools
natuals = itertools.count()#无限迭代器
for n in natuals:
    print (n)

#cycle()会把传入的一个序列无限重复下去
import itertools
cs = itertools.cycle('ABC')
for c in cs:
    print (c)
'''
#repeat()负责把一个元素无限重复下去，可以限定重复次数
import itertools
ns = itertools.repeat('A',3)
for n in ns:
    print (n)

#通过takewhile()等函数根据条件判断来截取出一个有限的序列
import itertools
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print (list(ns))

#chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('ABC', 'XYZ'):
    print (c)

#groupby()把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('AAcBBBCCAAA'):
    print(key, list(group))

for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))


#contextlib,实现上下文管理是通过__enter__和__exit__这两个方法实现的
from contextlib import contextmanager
class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print ('Begin')
    q  =Query(name)
    yield q
    print ('End')

with create_query('Bob') as q:
    q.query()

@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")

'''
代码的执行顺序是：
with语句首先执行yield之前的语句，因此打印出<h1>；
yield调用会执行with语句内部的所有语句，因此打印出hello和world；
最后执行yield之后的语句，打印出</h1>。
'''

'''
@closing
如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，
可以用closing()来把该对象变为上下文对象。例如，用with语句使用urlopen()
'''
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print (line)

@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()

#urllib提供了一系列用于操作URL的功能。
#Get
#对豆瓣的一个URLhttps://api.douban.com/v2/book/2129650进行抓取，并返回响应
from urllib import request

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))

#模拟iPhone 6去请求百度首页
from urllib import request

req = request.Request('http://www.baidu.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

#Post,如果要以POST发送一个请求，只需要把参数data以bytes形式传入
#模拟一个微博登录，先读取登录的邮箱和口令，然后按照weibo.cn的登录页的格式以username=xxx&password=xxx的编码传入
from urllib import request, parse

print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

#Handler,通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理
'''
proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
    pass
'''

#HTMLParser,解析HTML
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')