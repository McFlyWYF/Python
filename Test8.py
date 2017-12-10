class Student(object):
    pass


s = Student()
s.name = 'Mick'


# 定义一个函数作为实例方法
def set_age(self, age):
    self.age = age


from types import MethodType

# 给实例绑定一个方法
s.set_age = MethodType(set_age, s)
# 调用实例方法
s.set_age(25)
print(s.age)


# 给一个实例绑定的方法，对其他实例不起作用
# s2 = Student()
# s2.set_age(20)

# 给所有实例绑定方法,可以给class帮定方法
def set_score(self, score):
    self.score = score


Student.set_score = set_score
s3 = Student()
s4 = Student()

s3.set_score(100)
print(s3.score)

s4.set_score(90)
print(s4.score)


# 使用__slots__
# 定义一个特殊的__slots__变量，来限制该class实例能添加的属性
class Student(object):
    __slots__ = ('name', 'age')


s = Student()
s.name = "James"
s.age = 20


# s.score = 100
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
class GraduateStudent(Student):
    pass


g = GraduateStudent()
g.score = 30
print(g.score)

print('********************************************')


# 使用@property
class Student(object):
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('please input int')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100')
        self._score = value


s = Student()
s.set_score(80)
print(s.get_score())


# Python内置的@property装饰器就是负责把一个方法变成属性调用的
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('please input int')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100')
        self._score = value


# 把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了
# 另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
s = Student()
s.score = 60  # 实际转化为s.set_score(60)
print(s.score)  # 实际转化为s.get_score()


# 只定义只读属性
class Student(object):
    @property
    def brith(self):
        return self._brith

    @brith.setter
    def brith(self, value):
        self._brith = value

    @property
    def age(self):
        return 2015 - self._brith


s = Student()
# brith是可读可写属性
s.brith = 2017
print(s.brith)
# age是只读属性
print(s.age)


# 多重继承
class Animal(object):
    pass


# 大类
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


# 各种动物

class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass


class Runnable(object):
    def run(self):
        print('Running...')


class Flyable(object):
    def fly(self):
        print('Flying...')


class Dog(Mammal, Runnable):
    pass


class Bat(Mammal, Flyable):
    pass


# 对需要 Fly 和 Run 方法的直接继承 Runnable、Flyable 类即可
s = Bat()
s.fly()


# 定制类
class Student(object):
    def __init__(self, name):
        self.name = name;

    # __str()__返回一个字符串
    def __str__(self):
        return 'Student object (name:%s)' % self.name

    __repr__ = __str__  # 可以这样写


print(Student('Mick'))

# __str()__返回用户看到的字符串，__repr()__返回开发者看到的字符串，是为调试服务的
s = Student('Mick')
print(s)


# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
# 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法
# 拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化计时器

    def __iter__(self):  # 自身是迭代对象，返回自己
        return self

    def __next__(self):
        self.a, self.b = self.b, self.b + self.a  # 计算下一个值

        if self.a > 10000:
            raise StopIteration()
        return self.a  # 返回下一个值


for n in Fib():
    print(n)


# 表现得像list那样按照下标取出元素，需要实现__getitem__()方法
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


f = Fib()
print(f[0])
print(f[3])


# 仿照list的切片方法
class Fib(object):
    def __getitem__(self, item):
        if isinstance(item, int):  # item是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(item, slice):  # item 是切片
            start = item.start
            stop = item.stop
            if start is None:
                start = 0

            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b

            return L


f = Fib()
print(f[0:5])
print(f[:10])
print(f[:5:2])


# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。
# 最后，还有一个__delitem__()方法，用于删除某个元素。

# __getattr()__方法，动态返回一个属性
class Student(object):
    def __init__(self):
        self.name = "Mick"

    def __getattr__(self, item):
        if item == 'score':
            return 99
            # 或者return lambda : 25
        raise AttributeError('Error')


# 前者调用方式是s.score,后者是s.score()
s = Student()
print(s.name)
print(s.score)


# print(s.num)
# print(s.score())


# __call()__ 直接在实例本身上调用
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s' % self.name)


s = Student('Mick')
print(s())

# 判断一个对象是否是可调用对象
print(callable(Student('Mick')))
print(callable(max))
print(callable([1, 2, 3]))
print(callable('str'))
print(callable(s))

# 使用枚举类
from enum import Enum

# 定义一个枚举类
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sep', 'Obt', 'Nov', 'Dec'))
# 枚举所有类型
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)  # value属性是自动给成员int变量
# 枚举单个类型
print(Month.Jan)

# 需要更精确的控制枚举类型，可以从Enum派生自定义类
from enum import Enum, unique


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wen = 3
    Thu = 4
    Fri = 5
    Sat = 6


# @unique 可以帮助我们检查有没有重复值
# 访问枚举类型
day1 = Weekday.Mon  # 用成员变量访问枚举类型
print(day1)
print(Weekday['Tue'])
print(Weekday.Thu.value)
print(day1 == Weekday.Mon)
print(Weekday(3))  # 根据value的值访问枚举类型
for name, member in Weekday.__members__.items():
    print(name, '=>', member)


# 使用元类
# type() 函数可以查看一个类型或变量的类型
class Hello(object):
    def hello(self, name='World'):
        print('%s' % name)


from Test8 import Hello

h = Hello()
h.hello()
print(type(Hello))
print(type(h))


# 通过type()函数创建一个 Hello 类
def fn(self, name="world"):
    print('Hello,%s' % name)


# 创建Hello类
Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()
h.hello()
print(type(Hello))
print(type(h))

# type()函数动态创建一个类
'''
创建类时，type()函数传入3个参数:
1.class的名称
2.继承的父类集合(注意tuple的单元素写法)
3.class的方法名称与函数绑定
'''
print('*******************************************')


# 控制类的创建行为，使用metaclass
# 先定义metaclass，然后创建类，最后创建实例
# metaclass可以创建类和修改类，把类看成是metaclass创建出来的实例
# 给MyList增加add()方法
class Listmetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=Listmetaclass):
    pass


'''
__new()__接收的参数是:
1.当前准备创建的类的对象
2.类的名字
3.类继承的父类集合
4.类的方法集合
'''

L = MyList()
L.add(1)
print(L)
