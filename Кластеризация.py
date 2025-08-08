import pandas as pd
import numpy as np

np.random.seed(42)
income = np.random.randint(20000, 120000, 100)
spending_score = np.random.randint(1, 101, 100)

data = pd.DataFrame({'Income': income, 'Spending Score': spending_score})
print(data.head())

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

X = data[['Income', 'Spending Score']]

kmeans = KMeans(n_clusters=3, random_state=42)
data['Cluster_KMeans'] = kmeans.fit_predict(X)

plt.figure(figsize=(8, 6))
plt.scatter(data['Income'], data['Spending Score'], c=data['Cluster_KMeans'], cmap='viridis', s=100)
plt.title('Кластеры клиентов')
plt.xlabel('Годовой доход')
plt.ylabel('Оценка затрат')
plt.show()

from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

discan = DBSCAN(eps=0.5, min_samples=5)
data['Cluster_DBSCAN'] = dbscan.fit_predict(X_scaled)

# Graph
plt.figure(figsize=(8, 6))
plt.scatter(data['Income'], data['Spending Score'], c=data['Cluster_DBSCAN'], cmap='plasma', s=100)
plt.title('Кластеры клиентов')
plt.xlabel('Годовой доход')
plt.ylabel('Оценка затрат')
plt.show()

from sklearn.decomposition import PCA

data['Age'] = np.random.randint(18, 70, 100)
data['Savings'] = np.random.randint(5000, 50000, 100)
data('Debt') = np.random.randint(1000, 20000, 100)

X_multidimensional = data[['Income', 'Spending Score', 'Age', 'Savings', 'Debt']]

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_multidimensional)

plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X[:, 1], c=data['Cluster_KMeans'], cmap='viridis', s=100)
plt.title('Данные после PCA')
plt.xlabel('Главная компонента 1')
plt.ylabel('Главная компонента 2')
plt.show()