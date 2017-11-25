# 高阶函数
print(abs(-1))
print(abs)

# 变量可以指向函数
x = abs(-10)
print(x)

x = abs
print(x)

# 直接调用abs()函数和调用变量f()完全相同
f = abs
print(f(-5))

# 函数名也是一个变量，可以通过给函数名赋值，修改函数的值
abs = 10
print(abs)

# 一个函数接收另一个函数作为参数，这种函数叫作高阶函数
'''
def add(x, y, f):
    return f(x) + f(y)

print(add(-2, 3, abs))
'''


# map() 和 reduce() 函数
# map()函数接收两个参数，一个是函数，一个是Iterable, map将传入的函数依次作用到序列的每一个元素，
# 并把结果作为新的Iterator返回
def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))
# 把list中所有元素转换为字符串
print(list(map(str, [1, 2, 3, 4, 5])))

# reduce,reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算.
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# 对一个序列求和
from functools import reduce


def add(x, y):
    return x + y


print(reduce(add, [1, 2, 3, 4, 5]))
print()

# str转换为int的函数
'''
from functools import reduce


def fn(x, y):
    return 10 * x + y

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4}[s]

print(reduce(fn, map(char2num, '13579')))
'''

print(list(map(int, ['1', '2', '3', '4', '5'])))


# filter 用于过滤序列，也接收一个函数和一个序列，和map不同的是，将传入的函数依次作用于每个元素，
# 根据返回值是True或False，决定保留还是舍弃该元素,filter()函数返回的是一个Iterator.
# 删掉偶数，保留奇数
def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7])))


# 删掉序列中的空字符串
def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['a', '', None, 'c', ' '])))
print()


# *********************输出素数**************************
# 生成器
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# 筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0


# 定义一个从2开始的生成器，不断返回下一个元素
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


for n in primes():
    if n < 100:
        print(n)
    else:
        break
# *****************************************************

# 用sorted()排序的关键在于实现一个映射函数.
# sorted可以对list进行排序
print(sorted([23, -4, -10, 5, 38]))

# sorted 还可以接受一个key函数实现自定义排序，如按绝对值进行排序
# print(sorted([23,-4,-10,5,38],key = abs))

# 默认情况下，对字符串排序，是按照ASCII的大小比较的
print(sorted(['bob', 'about', 'Zoo', 'Credit']))

# 忽略大小写进行排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))


# 返回函数
# 函数作为返回值
def lazy_sum(*args):
    def sum():
        ax = 0;
        for n in args:
            ax = ax + n
        return ax

    return sum


f = lazy_sum(1, 2, 3, 4, 5)
print(f)  # 返回的不是求和结果，而是sum函数
print(f())  # 返回的是求和结果

# 当我们调用lazy_sum函数时，即使参数相同，都会返回一个新的函数
f1 = lazy_sum(1, 2, 3)
f2 = lazy_sum(1, 2, 3)
print(f1 == f2)  # false


# 闭包
# 当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，
# 返回的函数并没有立刻执行，而是调用f()才会执行
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())


# 每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了。
# 你可能认为调用f1()，f2()和f3()结果应该是1，4，9,但结果是 9,9,9.
# 原因在于返回的结果引用了变量i,并非立刻执行，而是等到3个函数都返回时，i就变成了3
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

# 如果一定要引用循环变量的值，那就是再创建一个函数，用该函数的参数绑定当前循环变量的值
def count():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())

# 匿名函数
f = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(f)
# 匿名函数lambda x: x * x  其实就相当于 def f(x): return x * x
# 关键字 lambda 表示匿名函数，冒号前面 x 表示参数
# 匿名函数只能写一个表达式，不用写return，返回值就是结果
# 匿名函数也是一个函数对象，可以把匿名函数赋给一个变量，使用变量来调用
f = lambda x: x * x
print(f)
print(f(5))


# 也可以把匿名函数作为返回值返回
def build(x, y):
    return lambda x, y: x * x + y * y


print(build(1, 2))


# 装饰器
# 函数也是一个对象，可以通过变量来调用函数
def f():
    print("Hello World")


x = f
print(x())
print(f.__name__)  # 输出函数的名字
print(x.__name__)
print()


# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”(Decorator).
# decorator就是一个返回函数的高阶函数
# 装饰器
def log(func):
    def wrapper(*args, **kw):
        print("call %s():" % func.__name__)
        return func(*args, **kw)

    return wrapper


# @语法，把decorator置于函数的定义处
@log
def now():
    print("2017-11-25")


print(now())
print(now.__name__)


# @log 相当于 now = log(now)    print(now())

# ***********************************************************
# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数.
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print("%s %s():" % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log('execute')
def now():
    print("2017-11-25")


print(now())
print(now.__name__)  # now 函数名字变为 wrapper
# 三层嵌套的结果是 now = log('execute')(now)

# 通过 functools.wraps 可以把名字变为原来的 now
import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("call %s():" % func.__name__)
        return func(*args, **kw)

    return wrapper


print(now.__name__)

# 偏函数
# 通过设定参数的默认值，可以降低函数调用的难度,而偏函数也可以做到这一点.
x = int('12345')
print(x)

# int()函数还有base参数，默认为10,可以进行N进制转换
y = int('123',base=8)
print(y)
z = int('123',16)
print(z)

# ****************************************
def int2(x,base = 2):
    return int(x,base)

print(int2('1000000'))

# functools.partial就是帮助我们创建一个偏函数
import functools
int2 = functools.partial(int,base = 2)
print(int2('1000000'))

#简单总结functools.partial的作用就是，把一个函数的某些参数给固定住
# （也就是设置默认值），返回一个新的函数，调用这个新函数会更简单.
print(int2('1000000',base = 10))

# 创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
# 当传入 int2 = functools.partial(int,base = 2) 时
# 实际上固定了 base 的值，也就是 int2('10000')
# 相当于 kw = ['base' : 2]    int('10000',**kw)

# 当传入 max2 = functools.partial(max, 10)
# 实际上会把10作为*args的一部分自动加到左边,也就是 max2(5, 6, 7)
# 相当于 args = (10, 5, 6, 7)    max(*args)

max2 = functools.partial(max,10)
max2(5,6,7)
args = (10,5,6,7)
print(max(*args))