from itertools import combinations as cb
from bisect import bisect_right
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
arr = list(map(int,input().split()))
index = N//2 

a = arr[:index]
b = arr[index:]
a_list = [0]
b_list = [0]
for i in range(1,len(a)+1) :
    for j in cb(a, i) :
        a_list.append(sum(j))

for i in range(1,len(b)+1) :
    for j in cb(b, i) :
        b_list.append(sum(j))
a_list.sort()
b_list.sort()
count = 0

for i in a_list :
    count += bisect_right(b_list, M-i)
print(count)