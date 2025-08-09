def equal_monthly_payment(P, annual_rate, years):
    n = years * 12  # 总期数（月）
    r = annual_rate / 12  # 月利率

    # 每月固定还款额（等额本息公式）
    A = P * r * (1 + r) ** n / ((1 + r) ** n - 1)

    result = []
    remaining_principal = P

    for month in range(1, n + 1):
        interest = remaining_principal * r
        principal = A - interest
        remaining_principal -= principal

        result.append({
            'Month': month,
            'Payment': round(A, 2),
            'Principal': round(principal, 2),
            'Interest': round(interest, 2),
            'Remaining': round(max(remaining_principal, 0), 2)
        })

    return result


# 示例输入
P = float(input("请输入贷款金额（元）："))
annual_rate = float(input("请输入年利率（例如 0.05 表示5%）："))
years = int(input("请输入贷款期限（年）："))

# 获取还款计划
schedule = equal_monthly_payment(P, annual_rate, years)

# 打印表头
print(f"{'期数':>4} {'每月还款':>10} {'本金':>10} {'利息':>10} {'剩余本金':>12}")
for item in schedule:
    print(f"{item['Month']:>4} {item['Payment']:>10.2f} {item['Principal']:>10.2f} {item['Interest']:>10.2f} {item['Remaining']:>12.2f}")
