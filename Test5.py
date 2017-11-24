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
    it =_odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)

for n in primes():
    if n < 1000:
        print(n)
    else:
        break
# *****************************************************

# 用sorted()排序的关键在于实现一个映射函数.
# sorted可以对list进行排序
print(sorted([23,-4,-10,5,38]))

# sorted 还可以接受一个key函数实现自定义排序，如按绝对值进行排序
print(sorted([23,-4,-10,5,38],key = abs))

# 默认情况下，对字符串排序，是按照ASCII的大小比较的
print(sorted(['bob', 'about', 'Zoo', 'Credit']))

# 忽略大小写进行排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key = str.lower))

# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key = str.lower,reverse = True))