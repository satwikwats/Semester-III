import numpy as np
import matplotlib.pyplot as plt

def volu(d, N):
    n_hits=0
    for n in range(N):
        r=np.random.uniform(-1.0,1.0, d)
        radius=np.sqrt(np.sum(r**2))
        if radius<=1.0:
            n_hits+=1
    return n_hits*(2.0**d/N)

    

plt.scatter(dim, volume)

d=100
volume=[]
N=1000000
for i in range(d):
    volume.append(volu(i,N))
print(volume[99])
dim=np.arange(0,d,1)
