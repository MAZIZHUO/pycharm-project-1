import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic time series data
n_periods = 100
time = np.arange(n_periods)

trend = 0.5 * time
seasonality = 10 * np.sin(2 * np.pi * time / 12)
noise = np.random.normal(0, 5, n_periods)
y = trend + seasonality + noise

# Create DataFrame
df = pd.DataFrame({'time': time, 'y': y})
df['date'] = pd.date_range(start='2020-01-01', periods=n_periods, freq='M')
df.set_index('date', inplace=True)

# Plot the synthetic time series
plt.figure(figsize=(10, 4))
plt.plot(df.index, df['y'], label='Synthetic Time Series')
plt.title('Synthetic Time Series Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Add lag features
df['lag1'] = df['y'].shift(1)
df['lag2'] = df['y'].shift(2)
df.dropna(inplace=True)

# Prepare features and target
X = df[['lag1', 'lag2']]
y = df['y']

# Train-test split (80% train, 20% test)
split_index = int(len(df) * 0.8)
X_train, X_test = X[:split_index], X[split_index:]
y_train, y_test = y[:split_index], y[split_index:]

# Fit linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Plot actual vs predicted
plt.figure(figsize=(10, 4))
plt.plot(y_test.index, y_test, label='Actual')
plt.plot(y_test.index, y_pred, label='Predicted', linestyle='--')
plt.title('Linear Regression: Actual vs Predicted')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Evaluate model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error (MSE): {mse:.2f}')
print(f'R-squared (R²): {r2:.2f}')

# Show model coefficients
coef_df = pd.DataFrame({
    'Feature': ['lag1', 'lag2'],
    'Coefficient': model.coef_
})
print('\nRegression Coefficients:')
print(coef_df)
