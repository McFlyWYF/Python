print("Happy")
print(3 > 2)
print(True and False)
print(not True)

age = 3;
if age > 18:
    print("adult")
else:
    print("child")

    t = "happY"
    print(t)

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,Lisa!'''
print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)
print(r'Hello')

print(ord('A'))  # 获取字符整数标识
print(chr(97))  # 吧编码转换为对应字符
print(chr(25991))
print('\u4e2d\u6587')  # 十六进制
x = b'ABC'
print(x)
print('\n')
print('ABC'.encode('ascii'))  # 通过ascii转换为bytes
print('中文'.encode('utf-8'))  # 通过utf-8转换为bytes
print(b'ABC'.decode('ascii'))  # bytes转换为str
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

print(len('ABCDE'))  # 计算str包含多少个字符
print(len('中文'))

print(len(b'ABCDE'))  # 计算bytes包含的字节数
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))

print('Hi, %s,You have got %d score' % ('James', 98))  # 格式化
print('%2d-%02d' % (3, 1))
print('%.4f' % 3.1415926)
print('Age: %s Gender: %s' % (25, True))
print('growth %d %%' % 200)  # 使用 %% 来表示一个 %
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')

age1 = 8
if age1 >= 18:
    print('adult')
elif age1 >= 6:
    print('teenager')
else:
    print('child')

x = 1;  # 只要X非零，则输出True,否则输出False
if x:
    print('True')
else:
    print('False')

s = input('input your brith: ')  # input()函数返回的数据类型是str，使用int()函数将str类型转换为int
brith = int(s)
if brith < 2000:
    print('00前')
else:
    print('00后')

names = ['James', 'Bob', 'Love']  # for in  循环将字符串一次打印出来
for name in names:
    print(name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

sum1 = 0
for y in range(100):
    sum1 = sum1 + y
print(sum1)

sum2 = 0  # while循环
n = 99
while n > 0:
    sum2 = sum2 + n
    n = n - 1
print(sum2)

list = ['wang', 'zhang', 'li', 'zhao']
for s in list:
    print(s)

n = 10
while n > 0:

    if n < 5:
        break  # break的作用是提前结束循环
    print(n)
    n = n - 1
print('END')

m = 10
while m > 0:
    m = m - 1
    if m % 2 == 0:
        continue  # continue的作用是结束当前循环，开始下一次循环
    print(m)
print('END')

dict = {'james': 98, 'Bob': 0}  # 字典
print(dict['james'])

dict['Bob'] = 88
print(dict['Bob'])

dict.get('Bob', 0)  # 如果Key值不存在，可以通过此方法获得
print(dict['Bob'])

dict.pop("Bob")  # 使用pop()删除key
print(dict)

s = set([1, 2, 3, 3, 2])  # 重复 的元素杯过滤
print(s)

s.add(5)  # 添加元素
print(s)

s.remove(3)  # 删除元素
print(s)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])

print(s1 & s2)
print(s1 | s2)

b = ['c', 'b', 'a']  # list内部是可变的
b.sort()
print(b)

c = 'ABC'  # str是不可变的
print(c.replace('A', 'a'))
print(c)
