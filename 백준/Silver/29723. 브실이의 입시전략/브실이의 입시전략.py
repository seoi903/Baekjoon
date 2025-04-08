N, M, K = map(int, input().split())
subject = {}
for _ in range(N):
    s, p = input().split()
    subject[s] = int(p)

open_subject = 0
for _ in range(K):
    t = input()
    open_subject += subject[t]
    del subject[t]

subject = sorted(subject.items(), key=lambda x: x[1])
min_score, max_score = 0, 0
for i in range(M - K):
    min_score += subject[i][1]
    max_score += subject[-i - 1][1]

print(open_subject + min_score, open_subject + max_score)