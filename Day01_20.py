print('hello, world')
print('goodbye, world')

"""
第一个Python程序 - hello, world
Version: 1.0
Author: 骆昊
"""
# print('hello, world')
print("你好，世界！")

# 程序是数据和指令的有序集合，写程序就是用数据和指令控制计算机做我们想让它做的事情。
print(0b100)  # 二进制整数
print(0o100)  # 八进制整数
print(100)    # 十进制整数
print(0x100)  # 十六进制整数

print(123.456)    # 数学写法
print(1.23456e2)  # 科学计数法

"""
使用变量保存数据并进行加减乘除运算

Version: 1.0
Author: 骆昊
"""
a = 45        # 定义变量a，赋值45
b = 12        # 定义变量b，赋值12
print(a, b)   # 45 12
print(a + b)  # 57
print(a - b)  # 33
print(a * b)  # 540
print(a / b)  # 3.75

"""
使用type函数检查变量的类型

Version: 1.0
Author: 骆昊
"""
a = 100
b = 123.45
c = 'hello, world'
d = True
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'str'>
print(type(d))  # <class 'bool'>

"""
变量的类型转换操作

Version: 1.0
Author: 骆昊
"""
a = 100
b = 123.45
c = '123'
d = '100'
e = '123.45'
f = 'hello, world'
g = True
print(float(a))         # int类型的100转成float，输出100.0
print(int(b))           # float类型的123.45转成int，输出123
print(int(c))           # str类型的'123'转成int，输出123
print(int(c, base=16))  # str类型的'123'按十六进制转成int，输出291
print(int(d, base=2))   # str类型的'100'按二进制转成int，输出4
print(float(e))         # str类型的'123.45'转成float，输出123.45
print(bool(f))          # str类型的'hello, world'转成bool，输出True
print(int(g))           # bool类型的True转成int，输出1
print(chr(a))           # int类型的100转成str，输出'd'
print(ord('d'))         # str类型的'd'转成int，输出100

"""
算术运算符

Version: 1.0
Author: 骆昊
"""
print(321 + 12)     # 加法运算，输出333
print(321 - 12)     # 减法运算，输出309
print(321 * 12)     # 乘法运算，输出3852
print(321 / 12)     # 除法运算，输出26.75
print(321 // 12)    # 整除运算，输出26
print(321 % 12)     # 求模运算，输出9
print(321 ** 12)    # 求幂运算，输出1196906950228928915420617322241

"""
算术运算的优先级

Version: 1.0
Author: 骆昊
"""
print(2 + 3 * 5)           # 17
print((2 + 3) * 5)         # 25
print((2 + 3) * 5 ** 2)    # 125
print(((2 + 3) * 5) ** 2)  # 625

"""
赋值运算符和复合赋值运算符

Version: 1.0
Author: 骆昊
"""
a = 10
b = 3
a += b        # 相当于：a = a + b
a *= a + 2    # 相当于：a = a * (a + 2)
print(a)      # 大家算一下这里会输出什么

