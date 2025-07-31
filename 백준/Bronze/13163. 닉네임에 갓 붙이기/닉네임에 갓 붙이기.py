N = int(input())
 
for _ in range(N):
    nickName = input().split()
    result = "god"
 
    for i in range(1, len(nickName)):
        result += nickName[i]
 
    print(result)