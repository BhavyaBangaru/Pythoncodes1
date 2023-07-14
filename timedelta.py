import math
import os
import random
import re
import sys
from datetime import datetime
def time_delta(t1, t2):
    t1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    t2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    return abs(int((t2-t1).total_seconds()))
t = int(input())
for t_itr in range(t):
    t1 = input()
    t2 = input()
    delta = time_delta(t1, t2)
    print(delta)