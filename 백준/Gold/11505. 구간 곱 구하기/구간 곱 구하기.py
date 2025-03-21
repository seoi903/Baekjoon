import math
import sys

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()
MOD = 1000000007

n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

b = math.ceil(math.log2(n)) + 1
node_n = 1 << b
seg = [0 for _ in range(node_n)]

def make_seg(idx, s, e):
    
    if s == e:
        seg[idx] = arr[s]
        return seg[idx]

    mid = (s + e) // 2

    l = make_seg(idx * 2, s, mid)
    r = make_seg(idx * 2 + 1, mid + 1, e)
    seg[idx] = (l * r) % MOD

    return seg[idx]

def change(idx, s, e):
    
    if b - 1 < s or e < b - 1:  
        return seg[idx]

    if s == e:
        seg[idx] = new
        return new

    mid = (s + e) // 2

    l = change(idx * 2, s, mid)
    r = change(idx * 2 + 1, mid + 1, e)
    seg[idx] = (l * r) % MOD
    return seg[idx]

def get(idx, s, e):
    
    if to < s or e < frm:
        return 1

    mid = (s + e) // 2
    
    if frm <= s and e <= to:
        return seg[idx]

    else:
        l = get(idx * 2, s, mid)
        r = get(idx * 2 + 1, mid + 1, e)
        return (l * r) % MOD
    
make_seg(1, 0, len(arr) - 1)

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        cur = arr[b - 1]
        new = c
        change(1, 0, len(arr) - 1)
    else:
        frm, to = b - 1, c - 1
        print(get(1, 0, len(arr) - 1) % MOD)