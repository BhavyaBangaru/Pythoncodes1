import numpy as np
n=int(input())
arr=[]
for i in range(1,n+1):
    element=list(map(float,input().split()))
    arr.append(element)
print(round(np.linalg.det(arr),2))