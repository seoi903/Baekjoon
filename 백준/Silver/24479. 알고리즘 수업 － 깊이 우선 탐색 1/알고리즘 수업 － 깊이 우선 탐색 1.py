import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
path = []
result = [0]*(N+1)
visited = [-1]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, len(graph)):
    graph[i].sort()

def DFS(start):
    visited[start] = 1
    path.append(start)
    
    for adj_node in graph[start]:
        if visited[adj_node] == -1:
            DFS(adj_node)
    return

DFS(R)

for idx, node in zip(range(1, len(path)+1), path):
    result[node] = idx
    
print(*result[1:], sep="\n")