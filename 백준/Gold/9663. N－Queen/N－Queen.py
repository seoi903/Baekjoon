import sys
input = sys.stdin.readline
 
n = int(input())
 
def attack(x):
    for i in range(x): 
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return True
    return False
 
def dfs(start):
    global cnt
 
    if start == n:
        cnt += 1
    else:
        for i in range(n):
            row[start] = i
            if not attack(start):
                dfs(start + 1)
 
row = [0] * n
cnt = 0
dfs(0)
 
print(cnt)