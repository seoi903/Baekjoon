import sys
if __name__ == '__main__':
    for T in range(int(sys.stdin.readline().rstrip())):
        H, W = map(int, sys.stdin.readline().rstrip().split())
        grill = list()
        for _ in range(H):
            grill.append(sys.stdin.readline().rstrip())
        for now_grill in grill:
            print(now_grill[::-1])