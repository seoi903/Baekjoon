import sys

def gcd(A, B):
  while A * B != 0:
    if A > B:
      A = A % B
    else:
      B = B % A
  return A + B
      
input = sys.stdin.readline

A, B = map(int, input().rstrip().split())

G = gcd(A, B)
L = int((A * B) / G)

print(L)