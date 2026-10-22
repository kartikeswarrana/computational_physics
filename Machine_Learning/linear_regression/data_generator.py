import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng(seed=42)
a=2.1

b=0.8

x=np.mgrid[-10:11]
y=a*x+b
noise = rng.normal(loc=0, scale=1.2, size=y.shape)
noisy_data=y+noise
np.savez("data.npz",x=x,y=noisy_data)
stack = np.column_stack((x,noisy_data))
np.savetxt("data.csv",stack,delimiter=",",fmt="%.2f")
