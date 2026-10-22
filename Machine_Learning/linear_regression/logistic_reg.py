
import numpy as np
import matplotlib.pyplot as plt

# Training data
data = np.load("data_logi.npz")

X = data["x"].reshape(-1)
y = data["y"].reshape(-1)


# Initialize parameters
w = 0.0
b = 0.0
lr = 0.1
epochs = 1000
N = len(y)

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

loss_history = []

for epoch in range(epochs):
    # Forward pass
    z = w * X + b
    p = sigmoid(z)

    # Binary cross-entropy
    eps = 1e-12
    loss = -np.mean(
        y * np.log(p + eps)
        + (1 - y) * np.log(1 - p + eps)
    )
    loss_history.append(loss)

    # Gradients
    dw = np.mean((p - y) * X)
    db = np.mean(p - y)

    # Gradient descent
    w -= lr * dw
    b -= lr * db

# Predictions
p = sigmoid(w * X + b)
pred = (p >= 0.5).astype(int)

print("w =", w, "b =", b)
print("Probabilities:", np.round(p, 3))
print("Predictions:", pred)
print("Accuracy:", np.mean(pred == y))

# Plot 1: Data and learned probability curve
plt.figure(figsize=(8, 5))

plt.scatter(X, y, label="Actual labels", s=40)

X_plot = np.linspace(X.min(), X.max(), 300)
p_plot = sigmoid(w * X_plot + b)

plt.plot(X_plot, p_plot, "r", label="Predicted probability")
plt.axhline(0.5, color="gray", linestyle="--",
            label="Decision threshold")

plt.xlabel("X")
plt.ylabel("Probability of class 1")
plt.title("Logistic Regression")
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# Plot loss

plt.xlabel("Epoch")
plt.ylabel("Cross-entropy loss")
plt.show()
