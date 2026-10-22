import numpy as np
from tqdm import tqdm

data=np.load("data_5d_linear.npz")

X=data["X"]
y=data["y"].reshape(-1)

w=[0,0,0,0,0]
b=0
lr=1e-5
epochs=int(1e6)
N=len(y)


loss_history=[]

for epoch in tqdm(range(epochs)):
    y_pred = X@w+b
    error = y_pred - y

    loss=np.mean(error**2)
    loss_history.append(loss)

    dw=(2/N)*(X.T@error)
    db=(2/N)*np.sum(error)

    w = w - lr*dw
    b = b - lr*db


print(w)
print(b)
print(loss_history[-1])

#actual w=[1.1,4.2,3.6,0.7,0.8],b=1
