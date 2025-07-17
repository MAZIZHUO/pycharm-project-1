import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

# 1. Set random seed for reproducibility
np.random.seed(42)

# 2. Generate simulated volume data (e.g., random walk or AR(1) process)
n = 100
volume = np.random.normal(loc=1_000_000, scale=100_000, size=n).astype(int)

# 3. Generate close price as a function of lagged volume + noise
# Close_t = 0.00005 * Volume_{t-1} + noise
lagged_volume = np.roll(volume, 1)
lagged_volume[0] = volume[0]  # fix first value

noise = np.random.normal(loc=0, scale=5, size=n)
close_price = 0.00005 * lagged_volume + 100 + noise

# 4. Build DataFrame
data = pd.DataFrame({
    'Volume': volume,
    'Lagged_Volume': lagged_volume,
    'Close': close_price
})

# 5. Define regression variables
X = sm.add_constant(data['Lagged_Volume'])  # Add intercept
y = data['Close']

# 6. Fit regression model
model = sm.OLS(y, X).fit()
print(model.summary())

# 7. Predict and plot
data['Predicted_Close'] = model.predict(X)

plt.figure(figsize=(12, 6))
plt.plot(data['Close'], label='Actual Close Price', color='blue')
plt.plot(data['Predicted_Close'], label='Predicted Close Price', color='red', linestyle='--')
plt.title("Simulated Time Series Regression: Close ~ Lagged Volume")
plt.xlabel("Time Index")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

print(1+1)

