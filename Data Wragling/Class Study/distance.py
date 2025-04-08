import numpy as np
import pandas as pd
from scipy.spatial import distance
from scipy.stats import chi2

# ---------------------------
# 1. Create Sample Dataset
# ---------------------------
data = pd.DataFrame({
    'Index': range(1, 6),
    'Age': [25, 45, 31, 22, 35],
    'Income': [50000, 80000, 62000, 42000, 70000],
    'SpendingScore': [60, 30, 45, 70, 40],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Female']
})

# ---------------------------
# 2. Encode Gender (Binary)
# ---------------------------
data['Gender'] = data['Gender'].map({'Male': 0, 'Female': 1})

# ---------------------------
# 3. Define Query Point (Customer to compare)
# ---------------------------
query = np.array([30, 65000, 50, 0])  # Age, Income, Score, Gender

# ---------------------------
# 4. Distance Functions
# ---------------------------
def euclidean(x, y):
    return np.sqrt(np.sum((x - y) ** 2))

def manhattan(x, y):
    return np.sum(np.abs(x - y))

def minkowski(x, y, p):
    return np.sum(np.abs(x - y) ** p) ** (1 / p)

def chebyshev(x, y):
    return np.max(np.abs(x - y))

def cosine_sim(x, y):
    dot = np.dot(x, y)
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)
    return dot / (norm_x * norm_y)

def mahalanobis(x, data):
    cov = np.cov(data.T)
    inv_cov = np.linalg.inv(cov)
    diff = x - np.mean(data, axis=0)
    return np.sqrt(np.dot(np.dot(diff, inv_cov), diff.T))

# ---------------------------
# 5. Prepare Feature Matrix
# ---------------------------
features = data[['Age', 'Income', 'SpendingScore', 'Gender']].values

# ---------------------------
# 6. Apply Distances to All Rows
# ---------------------------
print("Distance from query [30, 65000, 50, Male]")
for i, row in enumerate(features):
    print(f"\nCustomer {data['Index'][i]}:")

    print("  Euclidean     :", round(euclidean(query, row), 2))
    print("  Manhattan     :", manhattan(query, row))
    print("  Minkowski(p=3):", round(minkowski(query, row, 3), 2))
    print("  Chebyshev     :", chebyshev(query, row))
    print("  Cosine Sim.   :", round(cosine_sim(query, row), 4))
    print("  Mahalanobis   :", round(mahalanobis(row, features), 2))