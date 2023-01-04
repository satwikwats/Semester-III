import numpy as np
import matplotlib.pyplot as plt
from numba import njit

@njit
def julia(z):
    n=0
    z0=0
    while abs(z)<20 and n<100:
        z = ((z**2 + 2)/(1+2*z))**2
        n = n + 1
    return n
  
x=np.linspace(-4.5,4.5,1000)
y=np.linspace(-4.5,4.5,1000)

meshx, meshy=np.meshgrid(x,y)
z= meshx +1j*meshy

image = np.zeros_like(z, dtype=int)


for i in range(1000):
    for j in range(1000):
        image[i, j] = julia(z[i, j])

plt.imshow(image, cmap="twilight")
plt.colorbar()
