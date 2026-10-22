import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

data=np.load("data.npz")

X=data["x"].reshape(-1)
y=data["y"].reshape(-1)

a,b=1,0.5

lr=0.001
N=len(X)
loss_history=[]
epoches=[]
training_a = []
training_b = []
training_y_pred =[]
for epoch in tqdm(range(50)):
    epoches.append(epoch)
    y_pred = a*X+b
    error = y_pred - y

    loss = np.mean(error**2)
    loss_history.append(loss)


    da=(2/N)*np.sum(error*X)
    db=(2/N)*np.sum(error)

    training_a.append(a)
    training_b.append(b)
    training_y_pred.append(y_pred.copy())

    b -= lr * db
    a -= lr * da

    



print(f"Slope a       = {a:.6f}")
print(f"Intercept b   = {b:.6f}")
print(f"Final MSE     = {loss_history[-1]:.6f}")

fig = plt.figure(figsize=(15, 5))

axes = [
    fig.add_subplot(131),
    fig.add_subplot(132),
    fig.add_subplot(133, projection="3d")
]

axes[0].scatter(X, y, s=15, label="Observed data")
axes[0].plot(X, (a * X + b),
         "r", label="Fitted line")
axes[0].set_xlabel("X")
axes[0].set_ylabel("y")
axes[0].legend()


axes[1].plot(epoches,loss_history)
axes[1].set_xlabel("Epoch")
axes[1].set_ylabel("MSE")

axes[2].plot3D(training_a, training_b, loss_history)
axes[2].set_xlabel("Slope a")
axes[2].set_ylabel("Intercept b")
axes[2].set_zlabel("MSE")

plt.show()