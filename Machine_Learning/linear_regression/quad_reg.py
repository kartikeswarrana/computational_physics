import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

data=np.load("data.npz")

X=data["x"].reshape(-1)
y=data["y"].reshape(-1)

a,b,c=0,0,0

lr=0.000001
N=len(X)
loss_history=[]
epoches=[]
training_a = []
training_b = []
training_y_pred =[]
for epoch in tqdm(range(500000)):
    epoches.append(epoch)
    y_pred = a*X**2+b*X+c
    error = y_pred - y

    loss = np.mean(error**2)
    loss_history.append(loss)


    da=(2/N)*np.sum(error*X**2)
    db=(2/N)*np.sum(error*X)
    dc=(2/N)*np.sum(error)

    training_a.append(a)
    training_b.append(b)
    training_y_pred.append(y_pred.copy())

    b -= lr * db
    a -= lr * da
    c -= lr * dc

    



print(f"a       = {a:.6f}")
print(f"b   = {b:.6f}")
print(f"c   = {c:.6f}")
print(f"Final MSE     = {loss_history[-1]:.6f}")

fig,axes = plt.subplots(1,2,figsize=(15, 5))


axes[0].scatter(X, y, s=15, label="Observed data")
axes[0].plot(X, a * X**2 + b * X + c,
         "r", label="Fitted line")
axes[0].set_xlabel("X")
axes[0].set_ylabel("y")
axes[0].legend()


axes[1].plot(epoches,loss_history)
axes[1].set_xlabel("Epoch")
axes[1].set_ylabel("MSE")



plt.show()