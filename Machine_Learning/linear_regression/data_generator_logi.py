import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng(seed=42)


x=np.linspace(1,20,21)
y = (x >= 10).astype(int)


np.savez("data_logi.npz",x=x,y=y)
stack = np.column_stack((x,y))
np.savetxt("data.csv",stack,delimiter=",",fmt="%.2f")