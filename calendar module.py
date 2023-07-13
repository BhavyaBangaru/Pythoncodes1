from calendar import *
Date=list(map(int,input().split()))
print(day_name[weekday(Date[2],Date[0],Date[1])].upper())