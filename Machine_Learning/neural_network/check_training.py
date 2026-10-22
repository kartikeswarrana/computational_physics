import numpy as np

# Load trained parameters
params = np.load("trained_nn_weights.npz")

W1 = params["W1"]
b1 = params["b1"]
W2 = params["W2"]
b2 = params["b2"]

def predict(X):
    Z1 = X @ W1 + b1
    H = np.maximum(0, Z1)  # ReLU
    y_pred = H @ W2 + b2
    return y_pred

# Load input data
data = np.load("data_5d_linear.npz")
X = data["X"]

predictions = predict(X)





x_new = np.array([[1.2, 3.4, 2.1, 0.5, 4.0]])

y_new = predict(x_new)
print("Given X:", x_new)
print("Predicted y:", y_new[0, 0])


y_true = data["y"].reshape(-1, 1)

mse = np.mean((predictions - y_true)**2)
print("MSE:", mse)




y_true = data["y"].reshape(-1, 1)

mse = np.mean((predictions - y_true)**2)
rmse = np.sqrt(mse)
mae = np.mean(np.abs(predictions - y_true))

print("MSE :", mse)
print("RMSE:", rmse)
print("MAE :", mae)

print("\nFirst 10 comparisons:")
for actual, predicted in zip(y_true[:10], predictions[:10]):
    print(f"actual={actual[0]:8.3f}  predicted={predicted[0]:8.3f}")