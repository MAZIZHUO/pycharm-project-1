#以下为if结构
"""
BMI计算器

Version: 1.0
Author: 骆昊
"""
height = float(input('身高(cm)：'))
weight = float(input('体重(kg)：'))
bmi = weight / (height / 100) ** 2
print(bmi)
print(f"bmi = {bmi}")
print(f"bmi完整 = {bmi}")  # 这是普通的 f-string，字符串里写了字面内容 "bmi = "，然后用 {bmi} 插入变量值。
print(f"{bmi = }")        # 这是 Python 3.8+ 的调试用格式，自动帮你输出变量名和变量值
print(f"{bmi = :.2f}")
print(round(bmi, 2))
if 18.5 <= bmi < 24:
    print('你的身材很棒！')

a = 2/3
print(a)
print(f'A = {a}') # 这是普通的 f-string
print(f'A = {a :.2f}')  #:是格式说明符（format specifier） 的分隔符，{变量:格式} → 用冒号 : 后面的格式规则来控制输出方式
print(f'A = {a = }')  # 这是 Python 3.8+ 的调试用格式，自动帮你输出变量名和变量值
print(f'A = {a = :.2f}')

#以下为 if-else 结构
h = 175
w = 70
b = w / (h / 100) ** 2
if 18.5 <= b < 24:
    print(f'你的BMI是{b :.2f},你的身材很棒!')
else:
    print('你的身材不够标准哟！')

#以下为if-elif-else结构
status_code = int(input('响应状态码: '))
if status_code == 400:
    description = 'Bad Request'
elif status_code == 401:
    description = 'Unauthorized'
elif status_code == 403:
    description = 'Forbidden'
elif status_code == 404:
    description = 'Not Found'
elif status_code == 405:
    description = 'Method Not Allowed'
elif status_code == 418:
    description = 'I am a teapot'
elif status_code == 429:
    description = 'Too many requests'
else:
    description = 'Unknown status Code'
print('状态码描述:', description)

#if-else案例
x = float(input('x = '))
if x < 0:
    y = x + 1
elif x == 0:
    y = x
else:
    y = x / (x + 1)
print(f'y = {y}')

