#文件读写

# 读取文件 open()函数,调用read()方法可以一次读取全部内容
f = open('E:\Test.txt','r')
print(f.read())
f.close()#如果读写文件时产生IOError,后面的f.close()就不会调用
#使用try...finally来实现文件关闭

try:
    f = open('E:\Test.txt','r')
    print(f.read())
finally:
    if f:
        f.close()

# with语句来自动调用close()方法
with open('E:\Test.txt','r') as f:
    print (f.read())

#read(size)方法，每次最多读取size个字节的内容，readline()每次读取一行内容
#readlines()一次读取所有内容并按行返回list

# file-like Object
#读取二进制文件'rb',比如图片，视频等等
f = open('E:\Test.jpg','rb')
print(f.read())

#字符编码，非UTF-8编码的文本文件，需要给open()函数传入encoding参数
f = open('E:\Test.txt','r',encoding = 'gbk')
print(f.read())

#open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理

#写文件
f = open('E:\Test.txt','w')
f.write('山西太原')
f.write('山西太原')#多次写入文件
f.close()
# 使用open('E:\Test.txt','a')可以在原有文件后面追加文字
print()

#StringIO(在内存中读写str)和BytesIO
from io import StringIO
f = StringIO()
print(f.write('hello'))
print(f.write(' '))
print(f.getvalue())#用于获得写入的str

f = StringIO('Hello\nHi\nGoodbye')
while True:
    s = f.readline()
    if s ==  '':
        break
    print(s.strip())

#BytesIO,操作二进制数据
from io import BytesIO
f = BytesIO()
print(f.write('中文'.encode('utf-8')))
print (f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())

#操作文件和目录
import os
print(os.name) #操作系统类型
#print(os.uname()) #查获取详细系统信息

#环境变量
print(os.environ)
print(os.environ.get('PATH')) #获取某个环境变量的值

#操作文件和目录
#操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中

#查看当前目录的绝对路径
print(os.path.abspath('.'))
#在某个目录下创建一个新目录,首先表示出完整路径
#print(os.path.join('E:\A','Test3'))
#print(os.mkdir('E:\A\Test3'))
#删掉一个目录
#print(os.rmdir('E:\A\Test1'))
#把一个路径拆分为两部分
print (os.path.split('E:\A\Test.txt'))
#直接得到扩展名
print (os.path.splitext('E:\A\Test.txt'))

#对文件重命名
#print(os.rename('E:\A\Test.jpg','E:\A\Test.txt'))
#删除文件
#print (os.remove('E:\A\Test.txt'))
#列出当前目录下的所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])
#列出所有的.py文件
print([x for x in os.listdir('.') if os.path.isdir(x) and os.path.splitext(x)[1] == '.py'])

#序列化(把变量从内存中变成可存储或传输的过程)
import pickle
d = dict(name = 'Bob',age = 20,score = 88)
print(pickle.dumps(d))
#pickle.dump()直接把对象序列化后写入Object,pickle.dumps()把任意对象序列化成一个bytes,存储在文件中

f = open('E:\A\Text.txt','wb')
print (pickle.dump(d,f))
f.close()

#反序列化
f = open('E:\A\Text.txt','rb')
d = pickle.load(f)
f.close()
print (d)

#JSON,JSON表示出的就是一个字符串
import json
d = dict(name = 'Bob',age = 20,score = 90)
print (json.dumps(d))
#把JSON对象反序列化为python对象
json_str = '{"name": "None", "age": 20, "score": 90}'
print (json.loads(json_str))

#JSON进阶
import json
class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score
     }
s = Student('Bob',20,99)
print (json.dumps(s,default = student2dict))

#反序列化
def dict2student(d):
    return Student(d['name'],d['age'],d['score'])
json_str = '{"name": "None", "age": 20, "score": 90}'
print (json.loads(json_str,object_hook = dict2student))