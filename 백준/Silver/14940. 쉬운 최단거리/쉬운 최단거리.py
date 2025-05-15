from collections import deque
import sys
def bfs (graph, visited, start):
    # 상하좌우 네 방향을 의미
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 큐 구현을 위한 deque 라이브러리 활용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start[0]][start[1]] = 0
    # 큐가 완전히 빌 때까지 반복
    while queue:
        # 큐에 삽입된 순서대로 노드 하나 꺼내기
        x,y = queue.popleft()
        # 현재 처리 중인 노드에서 방문하지 않은 인접 노드를 모두 큐에 삽입
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == -1 and graph[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y]+1; #방문표시
                    queue.append((nx, ny))
                

n, m  = map(int, sys.stdin.readline().split())
graph = [[0] *m for _ in range(n)]
visited = [[-1] *m for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, sys.stdin.readline().split()))
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start = (i,j)
        elif graph[i][j] == 0:
            visited[i][j] = 0

bfs(graph, visited, start)

#출력
for i in range(n):
    for j in range(m):
        print(visited[i][j], end=' ')
    print('')