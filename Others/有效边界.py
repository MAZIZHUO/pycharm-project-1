import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# ===============================
# 解决中文字体显示问题
# ===============================
plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题

# ===============================
# 1. 模拟股票数据
# ===============================
np.random.seed(42)
num_assets = 10
num_days = 252  # 一年交易日

# 模拟每日收益率
returns = np.random.normal(0.0005, 0.02, size=(num_days, num_assets))
df = pd.DataFrame(returns, columns=[f'股票{i+1}' for i in range(num_assets)])

# 年化收益率与协方差矩阵
mean_returns = df.mean() * 252
cov_matrix = df.cov() * 252

# ===============================
# 2. 投资组合绩效计算函数
# ===============================
def portfolio_performance(weights, mean_returns, cov_matrix):
    returns = np.dot(weights, mean_returns)
    volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    return returns, volatility

# ===============================
# 3. 有效前沿优化
# ===============================
def minimize_volatility(weights, mean_returns, cov_matrix, target_return):
    # 约束条件：组合收益率等于目标收益率
    constraints = (
        {'type': 'eq', 'fun': lambda w: np.dot(w, mean_returns) - target_return},
        {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}
    )
    bounds = tuple((0, 1) for _ in range(len(mean_returns)))
    result = minimize(lambda w: portfolio_performance(w, mean_returns, cov_matrix)[1],
                      x0=np.array(len(mean_returns) * [1. / len(mean_returns)]),
                      method='SLSQP', bounds=bounds, constraints=constraints)
    return result

target_returns = np.linspace(mean_returns.min(), mean_returns.max(), 50)
frontier_volatility = []

for r in target_returns:
    res = minimize_volatility(None, mean_returns, cov_matrix, r)
    if res.success:
        frontier_volatility.append(res.fun)
    else:
        frontier_volatility.append(np.nan)

# ===============================
# 4. 绘制有效前沿
# ===============================
plt.figure(figsize=(10, 6))
plt.plot(frontier_volatility, target_returns, 'g--', linewidth=2, label='有效前沿')

# 散点：随机投资组合
for _ in range(300):
    weights = np.random.dirichlet(np.ones(num_assets), size=1)[0]
    ret, vol = portfolio_performance(weights, mean_returns, cov_matrix)
    plt.scatter(vol, ret, c='skyblue', alpha=0.4, s=10)

plt.title("十只股票的模拟有效前沿", fontsize=14)
plt.xlabel("年化波动率", fontsize=12)
plt.ylabel("年化收益率", fontsize=12)
plt.legend()
plt.grid(True)
plt.show()
