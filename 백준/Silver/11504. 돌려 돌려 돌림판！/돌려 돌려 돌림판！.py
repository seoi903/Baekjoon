from sys import stdin

for _ in range(int(stdin.readline())):
    n, m = map(int, stdin.readline().split())
    x = int(''.join(list(stdin.readline().split())))
    y = int(''.join(list(stdin.readline().split())))
    data = list(map(int, stdin.readline().split()))
    data += data[:m]
    res = 0

    for i in range(n):
        check = int(''.join(map(str, data[i:i+m])))
        if x <= check <= y:
            res += 1

    print(res)