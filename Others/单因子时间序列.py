import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.stats.api as sms
import matplotlib.pyplot as plt

np.random.seed(42)
T = 100
alpha_true = 0.5
beta_true = 1.5
rho = 0.8  # 自相关系数
sigma_e = 1.0

# -----------------------------
# 1. 模拟因子收益 F_t
# -----------------------------
F = np.random.normal(0, 1, T)

# -----------------------------
# 2. 模拟自相关残差 ε_t
# ε_t = rho * ε_{t-1} + u_t
# -----------------------------
u = np.random.normal(0, sigma_e, T)
epsilon = np.zeros(T)
for t in range(1, T):
    epsilon[t] = rho * epsilon[t-1] + u[t]

# -----------------------------
# 3. 被解释变量 R_t
# -----------------------------
R = alpha_true + beta_true * F + epsilon
data = pd.DataFrame({'R': R, 'F': F})

# -----------------------------
# 4. 普通 OLS 回归
# -----------------------------
X = sm.add_constant(data['F'])
ols_model = sm.OLS(data['R'], X).fit()

# -----------------------------
# 5. 时间序列回归 (Newey-West 修正)
# -----------------------------
nw_model = sm.OLS(data['R'], X).fit(cov_type='HAC', cov_kwds={'maxlags':1})

# -----------------------------
# 6. 输出回归结果
# -----------------------------
print("===== OLS 回归 =====")
print(ols_model.summary())
print("\n===== Newey-West 时间序列回归 =====")
print(nw_model.summary())

# -----------------------------
# 7. 可视化回归线
# -----------------------------
plt.scatter(F, R, label='Simulated Data', color='gray')

# OLS 拟合线
plt.plot(F, ols_model.predict(X), color='blue', label='OLS Fit')

# Newey-West 拟合线
plt.plot(F, nw_model.predict(X), color='red', linestyle='--', label='Newey-West Fit')

plt.xlabel('Factor F')
plt.ylabel('Return R')
plt.title('OLS vs Time Series (Newey-West) Regression')
plt.legend()
plt.show()
