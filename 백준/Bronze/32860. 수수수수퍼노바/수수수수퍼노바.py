N, M = map(int, input().split())

lowercase = [''] + [chr(i) for i in range(ord('a'), ord('z') + 1)]
q = M // 26
r = M % 26

sn_id = ''

if M <= 26:
    sn_id = lowercase[M].upper()
elif r == 0:
    sn_id = lowercase[q - 1] + lowercase[-1]
else:
    sn_id = lowercase[q] + lowercase[r]

print(f'SN {N}{sn_id}')