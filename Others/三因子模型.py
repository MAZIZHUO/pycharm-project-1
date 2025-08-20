import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from matplotlib import rcParams

# ===== 设置字体（避免中文乱码） =====
rcParams['font.sans-serif'] = ['SimHei']  # 黑体
rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# ===== 1. 模拟数据 =====
np.random.seed(42)
T = 120  # 模拟120个月数据（10年）
n_portfolios = 6

# 三因子（模拟）
MKT = np.random.normal(0.01, 0.05, T)  # 市场超额收益
SMB = np.random.normal(0.0, 0.02, T)  # 规模因子
HML = np.random.normal(0.0, 0.02, T)  # 价值因子

factors = pd.DataFrame({
    'MKT': MKT,
    'SMB': SMB,
    'HML': HML
})

# 模拟6个投资组合的超额收益率
portfolios = {}
for i in range(n_portfolios):
    beta = np.random.uniform(0.8, 1.2)  # 市场beta
    s_coeff = np.random.uniform(-0.5, 0.5)
    h_coeff = np.random.uniform(-0.5, 0.5)
    alpha = np.random.uniform(-0.002, 0.002)

    noise = np.random.normal(0, 0.02, T)
    portfolios[f'组合{i + 1}'] = (alpha + beta * MKT + s_coeff * SMB + h_coeff * HML + noise)

portfolios = pd.DataFrame(portfolios)

# ===== 2. 回归分析 =====
results = {}
for col in portfolios.columns:
    y = portfolios[col]
    X = sm.add_constant(factors)
    model = sm.OLS(y, X).fit()
    results[col] = model
    print(f"\n{col} 回归结果：")
    print(model.summary())

# ===== 3. 可视化 =====
plt.figure(figsize=(12, 8))
for col in portfolios.columns:
    plt.plot(portfolios.index, portfolios[col], label=f"{col} 实际收益")
    plt.plot(portfolios.index, results[col].fittedvalues, '--', label=f"{col} 拟合收益")

plt.title("三因子模型：六个组合的实际收益 vs 拟合收益")
plt.xlabel("时间（月）")
plt.ylabel("超额收益率")
plt.legend()
plt.show()
