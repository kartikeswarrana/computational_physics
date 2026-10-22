import numpy as np

rng = np.random.default_rng(42)

w=[1.1,4.2,3.6,0.7,0.8]
b=1
N=500


X=rng.uniform(0.5,15,size=(N,5))


noise = rng.normal(loc=0, scale=1.5, size=N)

y=X@w+b+noise
print(y.shape)
print(X.shape)

x_test = rng.uniform(0.5, 15, size=5)

# True target, using the known parameters
y_test = x_test @ w + b 

print("Random input:", x_test)
print("True target:", y_test)

np.savez("data_5d_linear.npz",X=X,y=y)

