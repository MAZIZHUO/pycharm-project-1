import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# 生成模拟数据集
np.random.seed(42)
n_samples = 1000

# 创建特征变量
feature1 = np.random.normal(50, 10, n_samples)  # 平均50，标准差10的正态分布
feature2 = np.random.uniform(20, 80, n_samples)  # 20到80之间的均匀分布
feature3 = np.random.exponential(2, n_samples)   # 指数分布
feature4 = np.random.randint(1, 10, n_samples)  # 1到10之间的整数

# 创建目标变量（基于特征的线性组合加上噪声）
target = (2.5 * feature1 +
          1.3 * feature2 +
          3.2 * feature3 +
         -0.8 * feature4 +
          np.random.normal(0, 5, n_samples))  # 添加噪声

# 创建DataFrame
data = pd.DataFrame({
    'feature1': feature1,
    'feature2': feature2,
    'feature3': feature3,
    'feature4': feature4,
    'target': target
})

print("数据集前5行:")
print(data.head())
print("\n数据集基本信息:")
print(data.describe())

# 准备特征和目标变量
X = data[['feature1', 'feature2', 'feature3', 'feature4']]
y = data['target']

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建并训练多元线性回归模型
model = LinearRegression()
model.fit(X_train, y_train)

# 进行预测
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# 模型评估
train_mse = mean_squared_error(y_train, y_train_pred)
test_mse = mean_squared_error(y_test, y_test_pred)
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)

print("\n模型参数:")
print(f"截距项 (intercept): {model.intercept_:.2f}")
print("各特征系数 (coefficients):")
for i, coef in enumerate(model.coef_):
    print(f"  feature{i+1}: {coef:.2f}")

print("\n模型评估结果:")
print(f"训练集 MSE: {train_mse:.2f}")
print(f"测试集 MSE: {test_mse:.2f}")
print(f"训练集 R²: {train_r2:.4f}")
print(f"测试集 R²: {test_r2:.4f}")

# 可视化预测结果
plt.figure(figsize=(12, 5))

# 训练集预测结果
plt.subplot(1, 2, 1)
plt.scatter(y_train, y_train_pred, alpha=0.5)
plt.plot([y_train.min(), y_train.max()], [y_train.min(), y_train.max()], 'r--', lw=2)
plt.xlabel('实际值')
plt.ylabel('预测值')
plt.title(f'训练集预测结果 (R² = {train_r2:.4f})')

# 测试集预测结果
plt.subplot(1, 2, 2)
plt.scatter(y_test, y_test_pred, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('实际值')
plt.ylabel('预测值')
plt.title(f'测试集预测结果 (R² = {test_r2:.4f})')

plt.tight_layout()
plt.show()

# 预测新样本
new_sample = np.array([[50, 40, 2.5, 5]])
prediction = model.predict(new_sample)
print(f"\n新样本 {new_sample} 的预测值: {prediction[0]:.2f}")