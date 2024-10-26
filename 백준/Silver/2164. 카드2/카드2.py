import math

def find_last_card(N):
    M = 2 ** math.floor(math.log2(N))
    last_card = 2 * (N - M)
    return last_card if last_card != 0 else N

N=int(input())
print(find_last_card(N))