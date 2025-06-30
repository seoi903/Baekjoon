import sys
input= sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    li = list(map(int,input().split()))
    result = []
    while True: 
        new_li = []
        for i in range(len(li)-1):
            new_li.append( abs((li[i+1]-li[i])) ) 
        new_li.append(abs((li[-1]-li[0])))
        if new_li not in result:
            result.append(new_li)
            li= new_li
        else:
            result.append(new_li)
            li= new_li
            break

    k= result[-1]
    if sum(k) == 0:
        print("ZERO")
    else:#그렇지 않다면
        print("LOOP")