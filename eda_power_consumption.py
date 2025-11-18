import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'household_power_consumption.txt'
df = pd.read_csv(file_path, sep=';', low_memory=False, na_values='?')


df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], dayfirst=True)
df.set_index('DateTime', inplace=True)

print(df.head())
print(df.info())
print(df.isnull().sum())


plt.figure(figsize=(15, 6))
plt.plot(df.index, pd.to_numeric(df['Global_active_power'], errors='coerce'), label='Global Active Power')
plt.xlabel('Date Time')
plt.ylabel('Global Active Power (kilowatts)')
plt.title('Time Series of Global Active Power')
plt.legend()
plt.show()

# Visualize missing and zero values
missing_series = df['Global_active_power'].isnull()
zero_series = df['Global_active_power'] == '0'

plt.figure(figsize=(15, 3))
plt.plot(df.index, missing_series, 'r.', label='Missing Values')
plt.plot(df.index, zero_series, 'b.', label='Zero Values')
plt.xlabel('Date Time')
plt.title('Missing and Zero Values in Global Active Power')
plt.legend()
plt.show()

# Analyze hourly usage pattern
df['Hour'] = df.index.hour
hourly_avg = df.groupby('Hour')['Global_active_power'].apply(lambda x: pd.to_numeric(x, errors='coerce').mean())

plt.figure(figsize=(10, 5))
sns.barplot(x=hourly_avg.index, y=hourly_avg.values, palette='viridis')
plt.xlabel('Hour of Day')
plt.ylabel('Average Global Active Power')
plt.title('Average Hourly Power Consumption')
plt.show()
