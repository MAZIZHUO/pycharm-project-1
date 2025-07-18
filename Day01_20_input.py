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
print(f"{bmi = }")  # 这是 Python 3.8+ 的调试用格式，自动帮你输出变量名和变量值
print(f"{bmi = :.2f}")
print(round(bmi, 2))
if 18.5 <= bmi < 24:
    print('你的身材很棒！')


