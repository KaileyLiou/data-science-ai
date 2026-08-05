"""
DataDumper Loads Fashion MNIST training data from a CSV, splits into labels
and pixel features, normalizes features to 0-1 range, and prints
to verify load.
"""

# IMPORTS
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# LOAD DATA
df_train = pd.read_csv('fashion_mnist_20bal_train.csv')

# Extract labels from first column
y_train = df_train.iloc[:, 0]

# Extract features from remaining columns, normalize to 0-1 range
X_train = df_train.iloc[:, 1:] / 255.0

# Print dataset to verify load
print(df_train)
