N = int(input())
l=[]
for i in range(0,N):
    n=input().split()
    if n[0]=="print":
        print(l)
    elif n[0]=="insert":
        l.insert(int(n[1]),int(n[2]))
    elif n[0]=="remove":
        l.remove(int(n[1]))
    elif n[0]=="pop":
        l.pop()
    elif n[0]=="append":
        l.append(int(n[1]))
    elif n[0]=="sort":
        l.sort()
    else:
        l.reverse()