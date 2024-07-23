n = int(input())
a = list(map(int,input().split()))

min = a[0]
max = a[0]
for i in range(n):
    if max < a[i]:
        max = a[i]
    if min > a[i]:
        min = a[i]
print(min,max)
n = lnt(input())
a = list(map(int,input().split()))

print('{} {}'.format(min(a), max(a)))
