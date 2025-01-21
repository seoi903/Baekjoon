import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

import heapq

def dijkstra(start):
    q = []
    distance = [INF] * (n + 1)
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance
t = int(input())

for _ in range(t):

    n, m, k = map(int, input().split())
    s, g, h = map(int, input().split())
    INF = int(1e9)
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
        
    array = []
    
    for _ in range(k):
        array.append(int(input()))
        
    first = dijkstra(s)
    g_dijk = dijkstra(g)
    h_dijk = dijkstra(h)

    arr = []

    for b in array:
        if first[g] + g_dijk[h] + h_dijk[b] == first[b] or first[h] + h_dijk[g] + g_dijk[b] == first[b]:
            arr.append(b)

    arr.sort()

    for w in arr:
        print(w, end=' ')
        
    print()