import numpy as np
N,M=map(int,input().split())
arr=[]
for i in range(N):
    f=list(map(int, input().split()))
    arr.append(f)
print(np.max(np.min(np.array(arr),axis=1)))