import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. 生成模拟数据
np.random.seed(42)
n_samples = 100
X1 = 2 * np.random.rand(n_samples, 1)
X2 = 3 * np.random.rand(n_samples, 1)
# 真实模型: Y = 5 + 2*X1 + 3*X2 + 噪声
noise = np.random.randn(n_samples, 1)
Y = 5 + 2 * X1 + 3 * X2 + noise

# 合并自变量为一个矩阵
X = np.hstack([X1, X2])

# 2. 创建回归模型并训练
model = LinearRegression()
model.fit(X, Y)

# 3. 输出截距和系数
print(f'Intercept: {model.intercept_[0]:.3f}')
print(f'Coefficients: X1 = {model.coef_[0][0]:.3f}, X2 = {model.coef_[0][1]:.3f}')

# 4. 预测示例（选取部分样本）
Y_pred = model.predict(X)

# 5. 画出真实值 vs 预测值对比图
plt.figure(figsize=(8,6))
plt.scatter(Y, Y_pred, color='blue', alpha=0.6)
plt.plot([Y.min(), Y.max()], [Y.min(), Y.max()], 'r--', linewidth=2)
plt.xlabel('True Values')
plt.ylabel('Predicted Values')
plt.title('True vs Predicted Values (Multiple Linear Regression)')
plt.grid(True)
plt.show()
