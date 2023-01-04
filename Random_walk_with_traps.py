import numpy as np
import matplotlib.pyplot as plt

def randomwalk(n, steps):
    listt=np.zeros(n)
    for i in range(n):
        #for j in range(steps):
        x=0
        sum1=0
        x=2*np.random.randint(2, size=steps)-1
        for k in range(len(x)):
            sum1+=x[k]
            if sum1==10:
                listt[i]=k
                break
        
    return listt
  

n=10000
steps=10000
deaths=randomwalk(n,steps)
alive=np.zeros(n)
for i in range(len(deaths)):
    for j in range(int(deaths[i])):
        alive[j]+=1

frac = alive/n
N = np.arange(0,steps,1)
plt.scatter(N, frac, s=5)
plt.grid()
plt.show()
#plt.xlim(0,10)

        
# print(deaths)
# print(alive)
