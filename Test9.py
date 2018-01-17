# 错误处理
# try...except...finally...
try:
    print('try...')
    r = 10 / 0
    print('result:',r)

except ZeroDivisionError as e:
    print('except:',e)

finally:
    print('finally...')
print('END')
print()
# 使用try运行代码，如果执行出错，后续代码不会执行，而是直接跳转至错误处理代码，
# 即except语句块，执行完except后，如果有finally语句块，则执行finally语句块
# 如果没有错误，except语句块不会执行，但是finally一定会执行
# 可以有多个except语句块捕获不同类型的错误
try:
    print('try...')
    r = 10 / int('a')
    print('result:',r)

except ValueError as e:
    print('ValueError:',e)

except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)

else:
    print('no error')

finally:
    print('finally...')
print('END')

# 所有的错误类型都继承自BaseException
try:
    #foo()
    pass

except ValueError as e:
    print('ValueError')

except UnicodeError as e:
    print('UnicodeError')
#第二个except永远捕获不到UnicodeError，因为UnicodeError是ValueError的子类
# 使用try...except捕获错误的好处是可以跨越多层调用，比如，函数main()调用foo(),foo()调用bar(),bar()出错了，只要main()捕获到就可以处理
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s)*2

def main():
    try:
        bar('1')
    except Exception as e:
        print('Error:',e)
    else:
        print('no error')
    finally:
        print('finally...')

# 调用栈,如果没有捕获到错误，最终会被python解释器捕获到
'''
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s)*2

def main():
    bar('0')

main()
'''

# 记录错误
# 内置的logging模块可以记录错误信息
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s)*2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')
# 错误打印   ERROR:root:division by zero

# 抛出错误
# 自定义Exception，用raise语句抛出一个错误的实例
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 /a

foo('0')
print()
#另外一种错误处理机制
def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()
# raise语句如果不带参数，就会把错误原样抛出
# 在except中raise一个Error,会把一种类型的错误转化成另一种错误
try:
    10 / 0

except ZeroDivisionError:
    raise ValueError('input error!')
# 不能把IOError转换成ValueError

#断言
#凡是可以用print()来查看的地方，都可以用断言assert来代替
def foo(s):
    n = int(s)
    assert n != 0,'n is zero'
    return 10/n

def main():
    foo('0')
#assert的意思是表达式 n != 0应该是True，否则抛出错误

# -0 参数可以关闭assert

#logging
#把print()替换为logging，logging不会抛出错误，而且可以输出到文件

import logging
logging.basicConfig(level = logging.INFO)
#它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，
# logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。这样一来，
# 你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。

#pdb
#Python调试器pdb,让程序单步运行
s = '0'
n = int(s)
print(10/n)
# 输入命令l来查看代码,输入命令n可以单步执行代码,输入命令p 变量名来查看变量,输入命令q结束调试，退出程序

#pdb.set_trace()，放在可能出错的地方
import pdb
s = '0'
n = int(s)
pdb.set_trace()
print(10/n)

# 单元测试
#文档测试