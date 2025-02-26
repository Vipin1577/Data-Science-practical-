# Import necessary libraries
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt

# Sample data (numerical features)
data = np.array([[1, 2], [3, 4], [5, 6]])

# Initialize the scalers
standard_scaler = StandardScaler()
min_max_scaler = MinMaxScaler()

# Apply Standardization (Z-Score Normalization)
standardized_data = standard_scaler.fit_transform(data)

# Apply Normalization (Min-Max Scaling)
normalized_data = min_max_scaler.fit_transform(data)

# Visualization of the original, standardized, and normalized data
fig, axs = plt.subplots(1, 3, figsize=(18, 5))

# Plot Original Data
axs[0].scatter(data[:, 0], data[:, 1], color='blue')
axs[0].set_title("Original Data")
axs[0].set_xlabel("Feature 1")
axs[0].set_ylabel("Feature 2")

# Plot Standardized Data
axs[1].scatter(standardized_data[:, 0], standardized_data[:, 1], color='green')
axs[1].set_title("Standardized Data (Z-Score)")
axs[1].set_xlabel("Feature 1")
axs[1].set_ylabel("Feature 2")

# Plot Normalized Data
axs[2].scatter(normalized_data[:, 0], normalized_data[:, 1], color='red')
axs[2].set_title("Normalized Data (Min-Max)")
axs[2].set_xlabel("Feature 1")
axs[2].set_ylabel("Feature 2")

# Show the plots
plt.tight_layout()
plt.show()

