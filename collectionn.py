from collections import namedtuple
N=int(input())
columns=list(map(str,input().split()))
Student=namedtuple('Student',columns)
print(sum([float(Student(*input().split()).MARKS) for i in range(N)])/N)