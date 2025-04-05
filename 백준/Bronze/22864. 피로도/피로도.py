import sys

a, b, c, m = map(int, sys.stdin.readline().split())
tired = 0
job = 0
for i in range(24):
    if tired < 0:
        tired = 0
    if tired + a <= m:
        tired += a
        job += b
    else:
        tired -= c
if tired > m:
    job = 0
print(job)