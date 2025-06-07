from sys import stdin
input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
   T = int(input())
   for _ in range(T):
       M = int(input())
       nums = []
       for _ in range(M // 10 + 1):
           nums += list(map(int, input().split()))

       print(M // 2 + 1)
       for i in range(1, len(nums) + 1, 2):
           print(sorted(nums[:i])[i // 2], end=' ')
       print()