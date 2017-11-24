# Python内置函数

# 调用函数
print(abs(100))  # 求绝对值
print(abs(-20))

print(max(1, 2, -1, 4))  # 返回最大的数
print(min(0, -3, 8, 19))  # 返回最小的数

print('\n')
print(int('123'))  # 字符转换为int
print(float('12.34'))
print(int(12.34))  # float转换为int
print(str(97))  # int 转换为str
print(str(1.23))
print(bool(1))  # int 转换为bool
print(bool(0))
print(bool(""))

a = abs  # 函数名就是一个指向函数对象的引用，可以把函数名赋给一个变量
print(a(-1))


# 定义函数

def my_abs(x):  # def  函数名(参数):  如果没有返回语句，会返回None
    if not isinstance(x, (int, float)):  # 如果不是 int 或 float 类型，则会抛出错误
        raise TypeError('Error')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-23))


# 空函数  内部什么事都不做，pass知识用来占位的

def nop():
    pass


import math


# 返回多个值,其实就是返回一个tuple
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
z = move(100, 100, 60, math.pi / 6)
print(x, y)
print(move(100, 100, 60, math.pi / 6))
print(z)


# 一元二次方程求解函数
def my_data(a, b, c):
    x1 = (-b + math.sqrt(b * b - 4 * a * c)) / 2 * a
    x2 = (-b - math.sqrt(b * b - 4 * a * c)) / 2 * a
    return x1, x2


n1, n2 = my_data(1, -2, -1)
print(n1, n2)

'''
import tensorflow as tf
hello = tf.constant("Hello TensorFlow")
sess = tf.Session()
print(sess.run(hello))

a = tf.constant(10)
b = tf.constant(20)
print(sess.run(a+b))
'''


# 函数的参数

# 位置参数
def power(x, n):
    s = 1;
    while n > 0:
        n = n - 1;
        s = s * x;
    return s


a = power(-1, 3)
print(a)


# 默认参数
def power(x, n=2):
    s = 1;
    while n > 0:
        n = n - 1;
        s = s * x;
    return s


b = power(5)
print(b)

c = power(2, 3)
print(c)


# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
def enroll(name, gender, age, school="NUC"):
    print("name: ", name)
    print("gender: ", gender)
    print("age: ", age)
    print("school: ", school)


enroll("wang", "M", 20)
enroll("zhang", "W", 18, "TYSchool")

'''默认参数必须指向不变对象！
主要是为了解决
print(add_end())
print(add_end())
['END']
['END', 'END']
'''


def add_end(list=None):
    if list is None:
        list = []
    list.append("END")
    return list


print(add_end([1, 2, 3]))

print(add_end())
print(add_end())


# 可变参数
def calc(*numbers):  # *numbers : tuple = ()
    sum = 0;
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2, 3))
print(calc())

list = [1, 2]
print(calc(list[0], list[1]))

# 简化代码
print(calc(*list))


# 关键字参数，关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def person(name, age, **kw):  # **kw : dict = {}
    print('name:', name, 'age:', age, 'other:', kw)


print(person('Bob', 20))
print(person('Green', 36, city='BeiJing'))
print(person('James', 52, gender='M', city='CAVS'))

# 简化代码
extra = {'city': 'TaiYuan', 'Job': 'Android'}
print(person('Jhon', 50, **extra))


# 命名关键字参数
# 如果其中有一个可变参数，后面可以不加 *
def person1(name, age, *args, city, job):
    print(name, age, args, city, job)


args = [1, 2, 3, 4]
print(person1('wang,', 26, args, city='ShangHai', job='Sale'))


# 命名关键字前面加必须 *
def person2(name, age, *, city, job):
    print(name, age, city, job)


print(person2('zhao', 30, city='GuangZhou', job='Business'))


# 参数组合
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def f1(a, b=0, *c, d, **e):
    print(a, b, c, d, e)


c = (1, 2, 3)
e = {'f': 12}
print(f1(1, 2, *c, d=0, **e))


# 注意 ：*args是可变参数，args接收的是一个tuple；
#       **kw是关键字参数，kw接收的是一个dict。
#       可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
#       关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。


# 递归函数
def fac(n):
    if n == 1:
        return 1
    return n * fac(n - 1)


print(fac(5))
print(fac(1))


# 递归调用的次数过多，会导致栈溢出,解决递归调用栈溢出的方法是通过尾递归优化.
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式,使递归本身无论调用多少次，都只占用一个栈帧.

# 尾递归
def fac(n):
    return fac_iter(n, 1)


def fac_iter(num, product):
    if num == 1:
        return product
    return fac_iter(num - 1, num * product)


print(fac(5))

print()
L = []
n = 1
while n <= 99:
    L.append(n)
    print(n)
    n = n + 2