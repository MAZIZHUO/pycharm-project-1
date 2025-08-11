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

