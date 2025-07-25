import sys, heapq

T = int(sys.stdin.readline())

for t in range(T):
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    dp = [[0 for _ in range(N)] for _ in range(N)]

    turn = True if N % 2 == 1 else False

    for size in range(N):
        
        for i in range(N - size):
            
            if size == 0:
                dp[i][i+size] = arr[i] if turn else 0
                
            elif turn:
                dp[i][i+size] = max(dp[i+1][i+size] + arr[i], dp[i][i+size-1] + arr[i+size])
                
            else:
                dp[i][i+size] = min(dp[i+1][i+size], dp[i][i+size-1])
            
        turn = not turn

    print(dp[0][N-1])