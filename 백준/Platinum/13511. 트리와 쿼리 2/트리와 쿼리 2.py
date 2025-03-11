import sys
from collections import deque
from math import log2

n = int(sys.stdin.readline())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, sys.stdin.readline().split())
    tree[a].append([b, c])
    tree[b].append([a, c])

depth = [0] * (n + 1)
parent = [[0, 0] for _ in range(n + 1)]
check = [False] * (n + 1)
q = deque([1])
check[1] = True
while q:
    now = q.popleft()
    for b, c in tree[now]:
        if not check[b]:
            q.append(b)
            depth[b] = depth[now] + 1
            parent[b][0] = now
            parent[b][1] = c
            check[b] = True

logN = int(log2(n) + 1)
dp = [[[0, 0] for _ in range(logN)] for __ in range(n + 1)]
for i in range(n + 1):
    dp[i][0][0] = parent[i][0]
    dp[i][0][1] = parent[i][1]

for j in range(1, logN):
    for i in range(1, n + 1):
        dp[i][j][0] = dp[dp[i][j - 1][0]][j - 1][0]
        dp[i][j][1] = dp[i][j - 1][1] + dp[dp[i][j - 1][0]][j - 1][1]

m = int(sys.stdin.readline())
for _ in range(m):
    I = list(map(int, sys.stdin.readline().split()))
    u, v = I[1], I[2]
    u2, v2 = u, v
    if depth[u2] < depth[v2]:
        u2, v2 = v2, u2
    diff = depth[u2] - depth[v2]
    for i in range(logN):
        if diff & 1 << i:
            u2 = dp[u2][i][0]
    if u2 == v2:
        lca = u2
    else:
        for i in range(logN - 1, -1, -1):
            if dp[u2][i][0] != dp[v2][i][0]:
                u2 = dp[u2][i][0]
                v2 = dp[v2][i][0]
        lca = dp[u2][0][0]

    if I[0] == 1:
        cost = 0
        diff_u = depth[u] - depth[lca]
        diff_v = depth[v] - depth[lca]
        for i in range(logN):
            if diff_u & 1 << i:
                cost += dp[u][i][1]
                u = dp[u][i][0]
            if diff_v & 1 << i:
                cost += dp[v][i][1]
                v = dp[v][i][0]
        print(cost)

    else:
        k = I[3]
        if k <= depth[u] - depth[lca]:
            diff = k - 1
            for i in range(logN):
                if diff & 1 << i:
                    u = dp[u][i][0]
            print(u)
        else:
            diff = depth[v] + depth[u] - 2 * depth[lca] - k + 1
            for i in range(logN - 1, -1, -1):
                if diff & 1 << i:
                    v = dp[v][i][0]
            print(v)