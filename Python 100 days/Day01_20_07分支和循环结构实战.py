"""
输出斐波那契数列中的前20个数

Version: 1.0
Author: 骆昊
"""

a, b = 0, 1
for _ in range(20):
    temp_a = b
    temp_b = a + b
    a = temp_a
    b = temp_b
    print(a)

a = 0
b = 1
for _ in range(20):
    temp_a = b
    temp_b = a + b
    a = temp_a
    b = temp_b
    print(a)

a = 0
b = 1
for _ in range(20):
    c = a + b
    a = b
    b = c
    print(a, b, c)

