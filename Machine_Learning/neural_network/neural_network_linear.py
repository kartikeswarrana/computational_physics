import numpy as np
from tqdm import tqdm

data=np.load("data_5d_linear.npz")

X=data["X"]
y=data["y"].reshape(-1,1)

N, n_input = X.shape
n_hidden=8
n_output=1

rng=np.random.default_rng(42)
W1=rng.normal(0,0.1,(n_input,n_hidden))
b1=np.zeros((1,n_hidden))

W2=rng.normal(0,0.1,(n_hidden,n_output))
b2=np.zeros((1,n_output))

lr=1e-5
epochs=int(1e6)
loss_history=[]
for epoch in tqdm(range(epochs)):

    Z1=X@W1+b1
    H=np.maximum(0,Z1) #ReLU
    y_pred = H@W2 +b2

    error = y_pred-y
    loss=np.mean(error**2)
    loss_history.append(loss)

    dY = (2/N)*error

    dW2=H.T@dY
    db2=np.sum(dY,axis=0,keepdims=True)

    dH=dY@W2.T
    dZ1=dH*(Z1>0)

    dW1=X.T@dZ1
    db1=np.sum(dZ1,axis=0,keepdims=True)


    W2-=lr*dW2
    b2-=lr*db2
    W1-=lr*dW1
    b1-=lr*db1


print("Final loss:", loss_history[-1])


np.savez(
    "trained_nn_weights.npz",
    W1=W1,
    b1=b1,
    W2=W2,
    b2=b2
)