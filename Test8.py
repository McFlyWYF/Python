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