from itertools import *
N=int(input())
List=input().split()
K=int(input())
count=0
for i in list(combinations(List,K)):
    if "a" in i :
        count += 1
print(count/len(list(combinations(List,K))))