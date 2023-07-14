import numpy as np
n,m=map(int,input().split())
l=np.array([input().split() for i in range(n)],int)
print(np.mean(l,axis=1))
print(np.var(l,axis=0))
print(round(np.std(l),11))