N=int(input())
dict1={}
for i in range(N):
    n,p,q,r=input().split()
    d=(float(p)+float(q)+float(r))/3
    dict1[n]=d
query_name=input()
print("%.2f"%round(dict1[query_name],2))