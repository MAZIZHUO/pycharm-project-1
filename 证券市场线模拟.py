import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体和负号正常显示（Windows系统示例）
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 微软雅黑字体
plt.rcParams['axes.unicode_minus'] = False

np.random.seed(42)

# 参数
num_stocks = 10
num_days = 252  # 一年交易日
rf = 0.02  # 无风险年收益率 2%
market_return_annual = 0.08  # 市场组合年收益率 8%

# 模拟市场每日收益率
market_daily_returns = np.random.normal(loc=market_return_annual/num_days, scale=0.01, size=num_days)

# 模拟10只股票的每日收益率，贝塔在0.5~1.5之间随机
betas = np.random.uniform(0.5, 1.5, num_stocks)

stock_daily_returns = np.array([
    rf/num_days + beta * (market_daily_returns - rf/num_days) + np.random.normal(0, 0.01, num_days)
    for beta in betas
])

# 计算年化收益率
stock_annual_returns = stock_daily_returns.mean(axis=1) * 252
market_annual_return = market_daily_returns.mean() * 252

# 计算贝塔
betas_calc = []
for i in range(num_stocks):
    cov = np.cov(stock_daily_returns[i], market_daily_returns)[0,1]
    var = np.var(market_daily_returns)
    betas_calc.append(cov / var)
betas_calc = np.array(betas_calc)

# 绘制证券市场线
beta_range = np.linspace(0, 2, 100)
expected_return_sml = rf + beta_range * (market_annual_return - rf)

plt.figure(figsize=(10,6))
plt.plot(beta_range, expected_return_sml, label='证券市场线 (SML)', color='blue', linewidth=2)
plt.scatter(betas_calc, stock_annual_returns, color='red', label='股票实际收益与贝塔', s=50)

plt.xlabel('贝塔 (β)')
plt.ylabel('年化预期收益率')
plt.title('证券市场线（SML）示意图')
plt.legend()
plt.grid(True)
plt.show()
