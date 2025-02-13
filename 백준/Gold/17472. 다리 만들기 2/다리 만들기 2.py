import sys
from collections import deque
input = sys.stdin.readline

def find(x):
    if parent[x] < 0:
        return x
        
    parent[x] = find(parent[x])
    return parent[x]
    
def union(a, b):
    root_a = find(a)
    root_b = find(b)
    
    if root_a == root_b:
        return False
    
    if parent[root_a] < parent[root_b]:
        parent[root_b] = root_a
    elif parent[root_a] > parent[root_b]:
        parent[root_a] = root_b
    else:
        parent[root_a] = root_b
        parent[root_b] -= 1
    
    return True

def move():
    yield (-1, 0)
    yield (1, 0)
    yield (0, -1)
    yield (0, 1)

def BFS(start_x, start_y, island_num):
    visited[start_x][start_y] = True
    q = deque([(start_x, start_y)])
    island_search[(start_x, start_y)] = island_num
    island_cdns.append((island_num, start_x, start_y))
    
    while q:
        x, y = q.pop()
        
        for dx, dy in move():
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 1 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    island_search[(nx, ny)] = island_num
                    island_cdns.append((island_num, nx, ny))
                    q.appendleft((nx, ny))

N, M = map(int, input().split())
board = []

for _ in range(N):
    board.append([*map(int, input().split())])

visited = [[False]*M for _ in range(N)]
island_search = dict()
island_cdns = []
island_num = 0

for row in range(N):
    for col in range(M):
        if board[row][col] == 1 and visited[row][col] == False:
            island_num += 1
            BFS(row, col, island_num)

edges = []

for num, x, y in island_cdns:
    for dx, dy in move():
        nx = x + dx
        ny = y + dy
        dist = 0
        island_fin = None
        
        while True:
            if island_search.get((nx, ny)) == num:
                break
            
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                break
            
            if island_search.get((nx, ny)) != None and island_search.get((nx, ny)) != num:
                island_fin = island_search.get((nx, ny))
                break
            
            nx += dx
            ny += dy
            dist += 1
        
        if dist >= 2 and island_fin != None:
            edges.append((dist, num, island_fin))

edges.sort(reverse=True)
parent = [-1]*(island_num+1)
cnt = island_num-1
res = 0

while cnt:
    try:
        w, n1, n2 = edges.pop()
    except:
        res = -1
        break
    
    if union(n1, n2):
        res += w
        cnt -= 1

print(res)