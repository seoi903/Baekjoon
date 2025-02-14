import sys
sys.setrecursionlimit(1000000000)
N,R,Q=map(int,sys.stdin.readline().split(' '))


m=[[]for _ in range(N+1)]
visit=[-1 for _ in range(N+1)]

for _ in range(N-1):
    a,b=map(int,sys.stdin.readline().split(' '))
    m[a].append(b)
    m[b].append(a)

def dfs(now):
    global visit
    visit[now]=1
    for i in m[now]:
        if visit[i]==-1:
            visit[now]+=dfs(i) 
    return visit[now]
dfs(R)
for _ in range(Q):
    get=int(sys.stdin.readline())
    print(visit[get])