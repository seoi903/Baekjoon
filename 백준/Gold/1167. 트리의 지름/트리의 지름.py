from collections import deque
import sys
input = sys.stdin.readline
 
V = int(input())
graph = [[] for _ in range(V + 1)]
 
for _ in range(V):
    info = list(map(int, input().split()))
    for n in range(1, len(info) - 2, 2):
        graph[info[0]].append((info[n], info[n + 1])) # (연결노드, 거리)
 
def bfs(start):
    visited = [-1] * (V + 1)
    visited[start] = 0
    q = deque()
    q.append(start)
 
    while q:
        cur = q.popleft()
        for next, next_d in graph[cur]:
            if visited[next] == -1:
                q.append(next)
                visited[next] = visited[cur] + next_d
    
    m = max(visited)
    return [visited.index(m), m]
 
print(bfs(bfs(1)[0])[1])