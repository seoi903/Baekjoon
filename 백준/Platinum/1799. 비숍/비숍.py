import sys

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()
in_range = lambda y, x: 0 <= y < n and 0 <= x < n

n = int(input())
board = [[] for _ in range(n)]
for i in range(n):
    board[i] = list(map(int, input().split()))

rd = {}

for i in range(-n + 1, n):
    rd[i] = 0


def upper_bound(diag):
    able_rus = 0
    for d in range(diag, 2 * n - 1):
        for y in range(d + 1):
            x = d - y
            if in_range(y, x) and board[y][x] and rd[x - y] == 0:
                able_rus += 1
                break
    return able_rus

def f(diag, cnt):
    global ans
    if diag == 2 * n:
        ans = max(ans, cnt)
        return

    ub = upper_bound(diag)
    if ub + cnt <= ans:
        return
    
    for y in range(diag + 1):
        x = diag - y
        if in_range(y, x) and board[y][x] and rd[x - y] == 0:
            rd[x - y] = 1
            f(diag + 1, cnt + 1)
            rd[x - y] = 0

    f(diag + 1, cnt)
ans = 0
f(0, 0)
print(ans)