# 模块编程

'a test module'  # 任何模块的第一个字符串都被认为是注释
_author_ = 'wang'  # 作者

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello World')
    elif len(args) == 0:
        print('Hello, %s!' % args[1])
    else:
        print("Too many arguments!")


if __name__ == '__main__':
    test()

# 导入 Test6 模块，调用它的 test() 方法
import Test6

Test6.test()


# 作用域
# 正常的函数和变量名是公开的（public），可以被直接引用
# __xxx__这样的变量是特殊变量，可以被直接引用
# _xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用

# 实例
def _private_1(name):  # private 函数
    return 'Hello, %s' % name


def _private_2(name):  # private 函数
    return 'Hi,%s' % name


def greeting(name):  # public 函数
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

# 外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。

