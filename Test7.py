#面向对象编程
#使用原始方法
std1 = {'name':'James','score':90}
std2 = {'name':"Mick",'score':95}

def print_score(std):
    print('%s:%s'%(std['name'],std['score']))

print(print_score(std1))

#使用面向对象来实现
class Student(object):

    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s:%s'%(self.name,self.score))

James = Student('James',90)
Mick = Student('Mick',96)
# 调用对象的方法
James.print_score()
Mick.print_score()

#************************************************
#类的定义
#class关键字加类名，类名第一个字母大写，紧接着是(object),表示该类是从哪个类继承来的
#创建实例:类名+()实现的,如：A = Student()
class A(object):
    def __init__(self):
        pass
a = A()
b = A()
print(a)
print(b)
print(A)
'''
结果打印
<__main__.A object at 0x00000168BA2DA6D8>
<__main__.A object at 0x00000168BA2DA710>
<class '__main__.A'>
每个实例的地址都不一样
'''

# 可以给实例绑定任何一个属性
a.name = 'AAA'
print(a.name)

# 通过定义一个特殊的__init__方法，在创建实例的时候，就把必须绑定的属性绑上去：
# 注意：特殊方法“__init__”前后分别有两个下划线！！！
# 注意到__init__方法的第一个参数永远是self，表示创建的实例本身
# self不需要传
class B(object):
    def __init__(self,name,number):
        B.name = name
        B.number = number

b = B('BBB',12345)
print(b.name)
print(b.number)

#***********************************************************
# 数据封装
class C(object):
    def __init__(self,name,number):
        C.name = name
        C.number = number

    def print_number(self):
        print('%s:%s'%(self.name,self.number))
b = C('CCC',12345)
b.print_number()

# 封装的另一个好处是可以给Student类增加新的方法
class C(object):
    def __init__(self,name,score):
        C.name = name
        C.score = score

    def print_number(self):
        print('%s:%s'%(self.name,self.score))

    def get_grade(self):
        if(self.score >= 90):
            return 'A'

        elif(self.score > 60):
            return 'B'
        else:
            return 'C'

b = C('Mick',90)
b.print_number()
print(b.get_grade())
