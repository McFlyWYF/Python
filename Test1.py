import sys

print (sys.argv)

print("Hello World");print("中北大学")

if False:
    print("Answer")
    '''这是多行
    注释'''
    print("True")
else:
    print("Answer")
    print("False")
print('我是***') # 这是简单输出语句

import sys;
x = 'runoob'; print(x + '\n')
x = 'a';y = 'b';
print(x,y)     #不换行
print(x),print(y)

'''变量赋值不需要类型声明
在使用前必须赋值，赋值以后变量才会被创建
'''
count = 1  #整型
number = 2.6  #浮点数
name = "wang"  #字符串

print (count)
print(number)
print(name)

# 多个变量赋值
a = b = c = 1
d,e,f = 1,2.3,"jone"

print(a,b,c)
print(d,e,f)

'''标准数据类型
1.Numbers   数字
2.String   字符串
3.List   列表
4.Tuple   数组
5。Dictionary   字典
'''

#Python数字
'''数字数据类型存储数值,不可改变的数据类型'''

var1 = 1
var2 = 2
print(var1)

#删除对象引用
del  var1

#python支持4种数字类型
#   int  long   float  complex(复数)

#复数   实部和虚部都是浮点数
print(complex(1.1,2.2))

print(1.2 + 2.3j)

#获取子串,下标可以为空  可以是负数,变量名[头下标 : 尾下标]
a = "hello world this is china "
print(a[6:11])
print(a * 2)  #输出2次
print(a + "ok")  #连接字符串

#List 列表，有序的对象集合,包含  字符  数字  字符串   或者可以嵌套列表   用[]标识   也可以使用[:]截取
list = ['python',520,'a',23.45]
listadd = ['android']
print(list)  #输出整个列表
print(list[0])  #输出第一个元素   相当于数组
print(list[0:2])   #输出第一个  第二个元素
print(list * 2)  #输出两次
print(list + listadd)
#对第一个元素重新赋值
list[0] = "hello"
print(list)

#数组，也叫元组，类似于列表,用()标识，不能二次赋值
tuple = ('python',123,23.56,"hello world")
tupleadd = ('android')
print(tuple)
print(tuple[0])
print(tuple[0:3])
print(tuple * 2)
#下面语句无效,因为元组不允许二次赋值
#tuple[0] = "hello"
#print(tuple)

#字典，无序的对象集合，通过键来存取的，用“{}”标识，由索引key和值value组成
dict = {"name":"Jhon","number":123}
dict['one'] = "One"
dict[2] = "Two"
print(dict['one'])
print(dict[2])
print(dict.keys())
print(dict.values())
print(dict)

a = 111
if isinstance(a,int):
    print("True")
else:
    print("False")
