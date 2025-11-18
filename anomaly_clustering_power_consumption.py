import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns


file_path = 'household_power_consumption.txt'
df = pd.read_csv(file_path, sep=';', low_memory=False, na_values='?')
df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], dayfirst=True)
df.set_index('DateTime', inplace=True)
df['Global_active_power'] = pd.to_numeric(df['Global_active_power'], errors='coerce')
df = df.dropna(subset=['Global_active_power'])


X = df[['Global_active_power']].values
iso_forest = IsolationForest(contamination=0.01, random_state=42)
df['anomaly'] = iso_forest.fit_predict(X)


anomalies = df[df['anomaly'] == -1]
plt.figure(figsize=(14,6))
plt.plot(df.index, df['Global_active_power'], label='Normal')
plt.scatter(anomalies.index, anomalies['Global_active_power'],
            color='red', label='Anomaly', s=8)
plt.xlabel('DateTime')
plt.ylabel('Global Active Power')
plt.title('Anomaly Detection: Global Active Power')
plt.legend()
plt.show()

print(f"Detected {len(anomalies)} anomalies out of {len(df)} readings.")


# Aggregate to daily profiles by summing hourly means
df_daily = df.groupby(df.index.date).resample('H').mean()
df_daily = df_daily.reset_index()
df_daily = df_daily.pivot(index='Date', columns='DateTime', values='Global_active_power').fillna(0)
df_daily = df_daily.T

num_days = df_daily.shape[1]
print(f"Number of days in data: {num_days}")

n_clusters = 3  # low, medium, high usage
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
labels = kmeans.fit_predict(df_daily.T)

# Visualize clusters
plt.figure(figsize=(12,6))
for i in range(n_clusters):
    sns.lineplot(x=range(24), y=kmeans.cluster_centers_[i], label=f'Cluster {i+1}')
plt.xlabel('Hour of Day')
plt.ylabel('Average Power Usage (kW)')
plt.title('Clustered Daily Power Profiles')
plt.legend()
plt.show()


df_clusters = pd.DataFrame({
    'Day': df_daily.columns,
    'Cluster': labels
})


for c in range(n_clusters):
    days_in_cluster = df_clusters[df_clusters['Cluster'] == c]['Day']
    print(f"\nCluster {c+1} has {len(days_in_cluster)} days.")
