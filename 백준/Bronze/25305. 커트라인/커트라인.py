import sys

input = sys.stdin.readline

N, k = map(int, input().split())

x_list = list(map(int, input().split()))

x_list.sort(reverse=True)

print(x_list[k-1])