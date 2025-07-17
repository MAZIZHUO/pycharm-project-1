import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

np.random.seed(42)

# 参数设置
n_days = 252
n_stocks = 10
rf = 0.01  # 无风险收益率 1%

# 模拟市场日收益率
market_returns = np.random.normal(loc=0.0005, scale=0.01, size=n_days)

# 为每只股票定义一个 β 和 α
betas = np.random.uniform(0.5, 1.5, n_stocks)
alphas = np.random.normal(0, 0.0002, n_stocks)

# 模拟股票日收益率： ri = α + β * rm + ε
epsilon = np.random.normal(0, 0.01, (n_days, n_stocks))
stock_returns = alphas + np.outer(market_returns, betas) + epsilon

# 转成 DataFrame
dates = pd.date_range("2023-01-01", periods=n_days, freq="B")
df_mkt = pd.DataFrame({'Market': market_returns}, index=dates)
df_stocks = pd.DataFrame(stock_returns, columns=[f"S{i+1}" for i in range(n_stocks)], index=dates)

# 计算超额收益
excess_mkt = df_mkt['Market'] - rf / 252
excess_ret = df_stocks.subtract(rf / 252, axis=0)

# 存储回归结果
betas_est, alphas_est = [], []

for stk in excess_ret.columns:
    X = sm.add_constant(excess_mkt)
    y = excess_ret[stk]
    model = sm.OLS(y, X).fit()
    alphas_est.append(model.params['const'])
    betas_est.append(model.params['Market'])

# 汇总结果
results = pd.DataFrame({
    'True β': betas,
    'Estimated β': betas_est,
    'Estimated α': alphas_est
})

print(results)


# 计算平均市场超额日收益 & 年化市场风险溢价
mean_excess_mkt = excess_mkt.mean() * 252
risk_premium = mean_excess_mkt  # 年化

# SML 线
beta_line = np.linspace(0, 2, 100)
sml = rf + beta_line * risk_premium

# 绘图
plt.figure(figsize=(10, 6))
plt.plot(beta_line, sml, label='Security Market Line', color='blue')

# 画出估计的点
for i, row in results.iterrows():
    plt.scatter(row['Estimated β'], rf + row['Estimated β'] * risk_premium,
                color='green')  # 理论值
    plt.scatter(row['Estimated β'], rf + row['Estimated β'] * risk_premium + row['Estimated α'],
                color='red')  # 实际值包含 α

plt.xlabel('Beta')
plt.ylabel('Expected Return')
plt.title('CAPM Empirical Test with Simulated Data')
plt.legend(['SML', 'Theoretical', 'Actual'])
plt.grid(True)
plt.show()
