import sys
input = lambda: sys.stdin.readline().rstrip()
from math import ceil, log

N, M, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

H = ceil(log(N, 2)+1)
tree = [0] * (2**H)

def init(l, r, node):
    if l == r:
        tree[node] = arr[l]
        return
    mid = (l+r) // 2
    init(l, mid, node*2)
    init(mid+1, r, node*2+1)
    tree[node] = tree[node*2] + tree[node*2+1]

init(0, N-1, 1)

def update(l, r, node, IDX, DIFF):
    if not (l <= IDX <= r):
        return
    tree[node] += DIFF
    if l == r:
        return
    mid = (l+r) // 2
    update(l, mid, node*2, IDX, DIFF)
    update(mid+1, r, node*2+1, IDX, DIFF)

def interval_sum(l, r, node, LEFT, RIGHT):
    if r < LEFT or RIGHT < l:
        return 0
    if LEFT <= l and r <= RIGHT:
        return tree[node]
    mid = (l+r) // 2
    return interval_sum(l, mid, node*2, LEFT, RIGHT) + interval_sum(mid+1, r, node*2+1, LEFT, RIGHT)

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        b -= 1
        update(0, N-1, 1, b, c-arr[b])
        arr[b] = c 
    else:
        b -= 1
        c -= 1
        print(interval_sum(0, N-1, 1, b, c))