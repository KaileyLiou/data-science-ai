"""
ClassViewer: Loads Fashion MNIST training data from a CSV, filters
by class number, and displays the first 20 images in a 4x5 grid.
"""

# IMPORTS
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# LOAD DATA
df = pd.read_csv('fashion_mnist_20bal_train.csv')

# SETTINGS
class_number = 7 # Class to display

# FILTER DATA
# Select first 20 rows matching class number
class_0_df = df[df['class'] == class_number].head(20)

# DISPLAY IMAGES
# Set up 4x5 grid of subplots
fig, axes = plt.subplots(nrows=4, ncols=5, figsize=(6, 4))

for i, row in enumerate(class_0_df.iterrows()):

    # Strip label, leaving only pixel values
    image_data = row[1][1:].values

    # Convert to unsigned integer for image display
    image_data = image_data.astype(np.uint8)

    # Reshape pixel values into 28x28 grid
    image_28x28 = image_data.reshape(28, 28)

    # Plot image in correct grid position
    ax = axes[i // 5, i % 5]
    ax.imshow(image_28x28, cmap='gray')
    ax.axis('off')

plt.tight_layout()
plt.show()