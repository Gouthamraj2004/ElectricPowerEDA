import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt


file_path = 'household_power_consumption.txt'
df = pd.read_csv(file_path, sep=';', low_memory=False, na_values='?')
df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], dayfirst=True)
df.set_index('DateTime', inplace=True)


df = df[['Global_active_power']].dropna()
df['Global_active_power'] = pd.to_numeric(df['Global_active_power'], errors='coerce')
df = df.dropna()


def create_windowed_data(series, n_steps=10):
    X, y = [], []
    for i in range(len(series) - n_steps):
        X.append(series[i:i + n_steps])
        y.append(series[i + n_steps])
    return np.array(X), np.array(y)

X, y = create_windowed_data(df['Global_active_power'].values, n_steps=10)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# Train simple Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.4f}")
print(f"Mean Absolute Error: {mae:.4f}")

# Plot predicted vs actual
plt.figure(figsize=(12,6))
plt.plot(np.arange(len(y_test)), y_test, label="Actual")
plt.plot(np.arange(len(y_pred)), y_pred, label="Predicted")
plt.xlabel("Test Sample Index")
plt.ylabel("Global Active Power")
plt.title("Predicted vs Actual Global Active Power")
plt.legend()
plt.show()
