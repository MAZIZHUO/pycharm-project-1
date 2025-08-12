import numpy as np
import numpy_financial as npf

def equal_payment_monthly(P, annual_rate, years):
    r = annual_rate / 12
    n = years * 12
    A = P * r * (1 + r) ** n / ((1 + r) ** n - 1)
    total = A * n
    return A, total

def cashflow_equal_payment(P, A, n):
    return [P] + [-A] * n

def cashflow_equal_principal(P, annual_rate, years):
    n = years * 12
    r = annual_rate / 12
    monthly_principal = P / n
    cashflows = [P]
    for i in range(n):
        remaining = P - monthly_principal * i
        interest = remaining * r
        payment = monthly_principal + interest
        cashflows.append(-payment)
    return cashflows

def compute_monthly_irr(cashflow):
    return npf.irr(cashflow)

# 用户输入
P = float(input("请输入贷款金额（元）："))
annual_rate = float(input("请输入年利率（如0.05表示5%）："))
years = int(input("请输入贷款期限（年）："))
n = years * 12

# 等额本息
A, total_equal_payment = equal_payment_monthly(P, annual_rate, years)
cf_equal_payment = cashflow_equal_payment(P, A, n)
irr_equal_payment_monthly = compute_monthly_irr(cf_equal_payment)
irr_equal_payment_simple_annual = irr_equal_payment_monthly * 12  # 简单年化

# 等额本金
cf_equal_principal = cashflow_equal_principal(P, annual_rate, years)
first_month_payment = -cf_equal_principal[1]
total_equal_principal = -sum(cf_equal_principal[1:])
irr_equal_principal_monthly = compute_monthly_irr(cf_equal_principal)
irr_equal_principal_simple_annual = irr_equal_principal_monthly * 12  # 简单年化

# 输出
print("\n📌 等额本息：")
print(f"  每月还款额：{A:.2f} 元")
print(f"  总还款额：{total_equal_payment:.2f} 元")
print(f"  实际 IRR（月利率）：{irr_equal_payment_monthly:.6%}")
print(f"  简单年化 IRR：{irr_equal_payment_simple_annual:.6%}")

print("\n📌 等额本金：")
print(f"  首月还款额：{first_month_payment:.2f} 元")
print(f"  总还款额：{total_equal_principal:.2f} 元")
print(f"  实际 IRR（月利率）：{irr_equal_principal_monthly:.6%}")
print(f"  简单年化 IRR：{irr_equal_principal_simple_annual:.6%}")
