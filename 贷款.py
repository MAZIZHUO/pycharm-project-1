import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font_path = 'C:/Windows/Fonts/simhei.ttf'  # 请确认此字体路径有效
font_prop = FontProperties(fname=font_path)


def loan_cashflows(principal, annual_rate, years):
    r = annual_rate / 12
    n = years * 12

    A = principal * (r * (1 + r) ** n) / ((1 + r) ** n - 1)

    eq_principal = np.zeros(n)
    eq_interest = np.zeros(n)

    fixed_principal = principal / n
    ep_principal = np.zeros(n)
    ep_interest = np.zeros(n)

    balance_eq = principal
    balance_ep = principal

    for month in range(n):
        interest_eq = balance_eq * r
        principal_eq = A - interest_eq
        balance_eq -= principal_eq
        eq_principal[month] = principal_eq
        eq_interest[month] = interest_eq

        interest_ep = balance_ep * r
        principal_ep = fixed_principal
        balance_ep -= principal_ep
        ep_principal[month] = principal_ep
        ep_interest[month] = interest_ep

    return (eq_principal, eq_interest), (ep_principal, ep_interest)


def plot_cashflows(principal, annual_rate, years):
    (eq_principal, eq_interest), (ep_principal, ep_interest) = loan_cashflows(principal, annual_rate, years)
    n = years * 12
    months = np.arange(1, n + 1)

    fig, axs = plt.subplots(2, 1, figsize=(14, 10))

    axs[0].bar(months, eq_principal, label='本金', color='tab:blue')
    axs[0].bar(months, eq_interest, bottom=eq_principal, label='利息', color='tab:orange', alpha=0.7)
    axs[0].set_title(f'等额本息还款拆分\n贷款金额: {principal}，年利率: {annual_rate * 100:.2f}%，期限: {years}年',
                     fontproperties=font_prop)
    axs[0].set_xlabel('月份', fontproperties=font_prop)
    axs[0].set_ylabel('金额（元）', fontproperties=font_prop)
    axs[0].legend(prop=font_prop)

    axs[1].bar(months, ep_principal, label='本金', color='tab:blue')
    axs[1].bar(months, ep_interest, bottom=ep_principal, label='利息', color='tab:orange', alpha=0.7)
    axs[1].set_title(f'等额本金还款拆分\n贷款金额: {principal}，年利率: {annual_rate * 100:.2f}%，期限: {years}年',
                     fontproperties=font_prop)
    axs[1].set_xlabel('月份', fontproperties=font_prop)
    axs[1].set_ylabel('金额（元）', fontproperties=font_prop)
    axs[1].legend(prop=font_prop)

    plt.tight_layout()
    plt.show()


principal = float(input("请输入贷款金额（元）："))
annual_rate = float(input("请输入年利率（如4%输入0.04）："))
years = int(input("请输入贷款期限（年）："))

plot_cashflows(principal, annual_rate, years)
