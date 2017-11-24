# 切片
# 对 list 进行切片
L = ['a', 'b', 'c', 'd', 'e']
r = []
n = 3
for i in range(n):
    r.append(L[i])
    print(r)

print(L[0:3])  # 可以使用切片简化操作
print(L[:3])  # 第一个索引0还可以省略
print(L[1:2])
print(L[-2:-1])  # 取倒数第二个元素

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(L[:10:2])  # 前10个数每两个数取一个
print(L[::5])  # 所有数每5个取一个
print(L[:])  # 原样复制L

# 对tuple进行切片，tuple不可变，操作结果仍是tuple
T = (0, 1, 2, 3, 4, 5)
print(T[:3])

# 字符串也可以用切片进行操作
S = 'ABCDEFGHI'
print(S[:3])
print(S[::2])

# 迭代
# 给定一个list或者是一个tuple,可以通过for循环来进行遍历，这种遍历称为迭代
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for key in d.values():  # 迭代的是 values
    print(key)

for k, v in d.items():  # 同时迭代 key 和 values
    print(k, v)

for ch in 'ABCD':  # 迭代字符串
    print(ch)

# 判断一个对象是否是可迭代对象，通过collections模块的Iterable类型判断

from collections import Iterable

print(isinstance('abc', Iterable))  # str是否可迭代
print(isinstance([1, 2, 3], Iterable))  # list是否可迭代
print(isinstance(123, Iterable))  # 整数是否可迭代

# enumerate函数可以把 list 变成索引元素对
for i, values in enumerate(['A', 'B', 'C']):
    print(i, values)

# 两个变量
for x, y in [(1, 2), (3, 4), (5, 6)]:
    print(x, y)

# 列表生成式
# 用来创建list的生成式
# 原始方法生成 [1x1,2x2,3x3,....]
L = []
for x in range(1, 11):
    L.append(x * x)
    print(L)

# 列表生成式代替上面原始方法
print([x * x for x in range(1, 11)])

# 也可以加上一下语句，输出偶数的平方
print([x * x for x in range(1, 11) if x % 2 == 0])

# 还可以使用两层循环生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])

# 三层循环，以下类似
print([m + n + l for m in '123' for n in 'ABC' for l in 'XYZ'])

# 列出当前目录下的所有文件和目录名
import os

print([d for d in os.listdir('.')])

# for 循环可以同时使用两个或多个变量
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, "=", v)

# 列表生成式可以使用两个变量来生成list
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])

# 把list 中的所有字符串变成小写
L = ['Hello', 'World', 'Android']
print([s.lower() for s in L])

# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错.
# 使用内建的isinstance函数判断一个变量是不是字符串
x = 123
y = 'abc'
print(isinstance(x, str))
print(isinstance(y, str))

# 生成器：一边循环一边计算(generator)
# 1.第一种方法创建一个generator
L = [x * x for x in range(10)]
print(L)

# 把 [] 改为 ()
g = (x * x for x in range(10))
print(g)

# 通过next()函数获得generator的下一个返回值
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# 使用for 循环遍历generator中的每一个元素
g = (x * x for x in range(10))
for n in g:
    print(n)


# 斐波那契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


# 输出斐波那契数列
print(fib(6))


# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator.
# 使用yield将fib函数变为generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


print(fib(6))

# 遍历打印
y = fib(6)
for n in y:
    print(n)

# 想要拿到generator的return语句的返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中.
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print("Generator return values", e.value)
        break

# 迭代器
'''
直接作用于for循环的数据类型有：
    list,tuple,dict,set,str,generator
    可以直接作用于for循环的对象统称为可迭代对象:Iterable
    使用isinstance()判断一个对象是否是可迭代对象
'''
from collections import Iterable

print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance((), Iterable))
print(isinstance(100, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print()

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator.
from collections import Iterator

print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance((), Iterator))
print(isinstance('abc', Iterator))
print(isinstance((x for x in range(10)), Iterator))
print()

# 生成器都是Iterator对象，但list，dict，str却不是Itreator对象
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数.
print(isinstance(iter([]),Iterator))
print(isinstance(iter('abc'),Iterator))

