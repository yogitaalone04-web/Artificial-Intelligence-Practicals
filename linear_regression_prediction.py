import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Given dataset
X = np.array([8, 2, 3]).reshape(-1, 1)
Y = np.array([5, 9, 1])

# Create and train model
model = LinearRegression()
model.fit(X, Y)

# Predictions
Y_pred = model.predict(X)

# Print results
print("Actual Y:", Y)
print("Predicted Y:", Y_pred)
print("Slope (m):", model.coef_[0])
print("Intercept (c):", model.intercept_)

# Plot graph
plt.scatter(X, Y) # actual data points
plt.plot(X, Y_pred) # regression line
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Linear Regression Graph")
plt.show()
