import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import warnings

from hmmlearn import hmm
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler

# === Усунення попереджень matplotlib ===
mdates._reset_internal_converters = lambda: None
warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")

# === 1. Генерація синтетичних даних енергоспоживання ===
np.random.seed(42)
dates = pd.date_range(start="2025-01-01", periods=200, freq="D")
# Синусоїда + шум
consumption = np.abs(np.sin(np.linspace(0, 20, 200)) * 50 + np.random.normal(0, 10, 200))

df = pd.DataFrame({'date': dates, 'consumption': consumption})
df.set_index('date', inplace=True)

# === 2. Підготовка даних для HMM ===
X = df['consumption'].values.reshape(-1, 1)

# === 3. Побудова та тренування Hidden Markov Model ===
model = hmm.GaussianHMM(n_components=3, covariance_type="diag", n_iter=1000, random_state=42)
model.fit(X)

# Прогноз поточних станів
hidden_states = model.predict(X)
df['HMM_state'] = hidden_states

# Прогноз наступного прихованого стану
next_state = model.predict([[df['consumption'].iloc[-1]]])[0]
print(f"🔮 Прогнозований наступний прихований стан (HMM): {next_state}")

# === 4. Масштабування даних для кластеризації ===
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# === 5. K-Means кластеризація ===
kmeans = KMeans(n_clusters=3, random_state=0)
df['KMeans_cluster'] = kmeans.fit_predict(X_scaled)

# === 6. DBSCAN кластеризація ===
dbscan = DBSCAN(eps=0.5, min_samples=5)
df['DBSCAN_cluster'] = dbscan.fit_predict(X_scaled)

# === 7. Візуалізація результатів ===
fig, axes = plt.subplots(3, 1, figsize=(12, 10), sharex=True)

# HMM
df['consumption'].plot(ax=axes[0], color='black')
axes[0].set_title("Hidden Markov Model States")
for state in np.unique(df['HMM_state']):
    axes[0].plot(df[df['HMM_state'] == state].index,
                 df[df['HMM_state'] == state]['consumption'],
                 '.', label=f"State {state}")
axes[0].legend()

# KMeans
df['consumption'].plot(ax=axes[1], color='black')
axes[1].set_title("KMeans Clustering")
for cl in np.unique(df['KMeans_cluster']):
    axes[1].plot(df[df['KMeans_cluster'] == cl].index,
                 df[df['KMeans_cluster'] == cl]['consumption'],
                 '.', label=f"Cluster {cl}")
axes[1].legend()

# DBSCAN
df['consumption'].plot(ax=axes[2], color='black')
axes[2].set_title("DBSCAN Clustering")
for cl in np.unique(df['DBSCAN_cluster']):
    axes[2].plot(df[df['DBSCAN_cluster'] == cl].index,
                 df[df['DBSCAN_cluster'] == cl]['consumption'],
                 '.', label=f"Cluster {cl}")
axes[2].legend()

plt.tight_layout()
plt.show()
