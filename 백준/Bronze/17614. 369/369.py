# 입력
n = int(input())

# 브루트포스
cnt = 0  # 박수 친 횟수
for num in range(1, n+1):
    for i in str(num):
        if i == '3' or i == '6' or i == '9':
            cnt += 1
print(cnt)