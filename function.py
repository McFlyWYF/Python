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
    x1 = (-b + math.sqrt(b * b - 4 * a * c)) / 2*a
    x2 = (-b - math.sqrt(b * b - 4 * a * c)) / 2*a
    return x1,x2

n1,n2 = my_data(1,-2,-1)
print(n1,n2)

