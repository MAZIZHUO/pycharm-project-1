import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.regression.linear_model import OLS
from statsmodels.tools import add_constant
from arch import arch_model
from pmdarima.arima.utils import ndiffs
from statsmodels.tsa.statespace.kalman_filter import KalmanFilter

np.random.seed(42)

# ===== 1. 模拟数据 =====
T = 500  # 时间长度
mu_m, sigma_m = 0.001, 0.02  # 市场收益均值和波动率
mu_i, sigma_i = 0.001, 0.03  # 股票收益均值和波动率
beta_true = 1.2

# 模拟市场收益
R_m = np.random.normal(mu_m, sigma_m, T)
# 股票收益: R_i = alpha + beta*R_m + epsilon
epsilon = np.random.normal(0, sigma_i, T)
R_i = 0.0005 + beta_true * R_m + epsilon

data = pd.DataFrame({'R_i': R_i, 'R_m': R_m})

# ===== 2. 经典OLS =====
X = add_constant(data['R_m'])
ols_model = OLS(data['R_i'], X).fit()
beta_ols = ols_model.params['R_m']
print("OLS β:", beta_ols)

# ===== 3. 滚动窗口 β =====
window = 50
rolling_beta = data['R_i'].rolling(window).cov(data['R_m']) / data['R_m'].rolling(window).var()
rolling_beta.plot(title='Rolling β (window=50)')
plt.show()

# ===== 4. EWMA加权历史 β =====
lambda_ = 0.94
weights = np.array([lambda_**i for i in range(window-1, -1, -1)])
def ewma_beta(x, y, weights):
    cov = np.cov(x, y, aweights=weights)[0,1]
    var = np.cov(x, x, aweights=weights)[0,0]
    return cov / var

ewma_betas = []
for i in range(window, T+1):
    ewma_betas.append(ewma_beta(data['R_i'].iloc[i-window:i], data['R_m'].iloc[i-window:i], weights))
pd.Series(ewma_betas, index=data.index[window-1:]).plot(title='EWMA β')
plt.show()

# ===== 5. GARCH条件β =====
# 我们用一个简单的ARCH(1)模型估计股票和市场条件波动率，然后计算条件β
# 注意：这里是演示，实际DCC-GARCH需要更复杂的包如 'arch' + 'mgarch'
am_i = arch_model(data['R_i'], vol='Garch', p=1, q=1, dist='normal').fit(disp="off")
am_m = arch_model(data['R_m'], vol='Garch', p=1, q=1, dist='normal').fit(disp="off")

cond_var_i = am_i.conditional_volatility**2
cond_var_m = am_m.conditional_volatility**2
cond_cov = data['R_i'].rolling(window).cov(data['R_m'])  # 简化近似
beta_garch = cond_cov / cond_var_m
beta_garch.plot(title='Approx. Conditional β (GARCH)')
plt.show()

# ===== 6. Kalman滤波动态β =====
# 这里用简单状态空间模型近似
from pykalman import KalmanFilter

kf = KalmanFilter(
    transition_matrices = [1],
    observation_matrices = [data['R_m'].values.reshape(-1,1)],
    initial_state_mean = 0,
    initial_state_covariance = 1,
    observation_covariance=1,
    transition_covariance=0.01
)
state_means, state_covs = kf.filter(data['R_i'].values)
pd.Series(state_means.flatten(), index=data.index).plot(title='Kalman Filter β')
plt.show()
