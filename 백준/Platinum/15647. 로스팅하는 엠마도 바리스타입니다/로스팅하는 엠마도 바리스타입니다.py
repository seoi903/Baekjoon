import sys

sys.setrecursionlimit(600_000)
input = sys.stdin.buffer.readline

N = int(input())
adj = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v, d = map(int, input().split())
    adj[u].append((v, d))
    adj[v].append((u, d))

sub_size   = [0] * (N + 1) 
dist_sum   = [0] * (N + 1) 
depth      = [0] * (N + 1) 
parent     = [0] * (N + 1)

order = []
stack = [1]
parent[1] = -1 

while stack: 
    u = stack.pop()
    order.append(u)
    for v, w in adj[u]:
        if v == parent[u]:
            continue
        parent[v] = u
        depth[v] = depth[u] + w 
        stack.append(v)

for u in reversed(order):
    sub_size[u] = 1  
    for v, _ in adj[u]:
        if v == parent[u]:
            continue
        sub_size[u] += sub_size[v]

dist_sum[1] = sum(depth)

stack = [1]
while stack:
    u = stack.pop()
    for v, w in adj[u]:
        if v == parent[u]:
            continue
        dist_sum[v] = dist_sum[u] + (N - 2 * sub_size[v]) * w
        stack.append(v)

write = sys.stdout.write
write(''.join(f'{dist_sum[i]}\n' for i in range(1, N + 1)))