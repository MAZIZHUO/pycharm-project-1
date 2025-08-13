"""
从1到100的整数求和

Version: 1.0
Author: 骆昊
"""
total = 0
for i in range(1, 101):
    total = total + i
print(total)

t = 0
for i in range(1, 101):
    if i % 2 == 0:
        t = t + i
print(t)

"""
从1到100的整数求和

Version: 1.1
Author: 骆昊
"""
total = 0
i = 1
while i <= 100:
    total  = total + i
    i = i + 1
print(total)

"""
从1到100的偶数求和

Version: 1.3
Author: 骆昊
"""
total = 0
i = 2
while i <= 100:
    total += i
    i += 2
print(total)

"""
从1到100的偶数求和

Version: 1.4
Author: 骆昊
"""
total = 0
i = 2
while True:
    total += i
    i += 2
    if i > 100:
        break
print(total)
