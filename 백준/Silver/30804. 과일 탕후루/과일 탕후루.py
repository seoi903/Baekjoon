N = int(input().strip())

fruit_num = list(map(int, input().strip().split()))

left = 0
fruit_count = {}
max_len = 0

for right in range(N):
    current_fruit = fruit_num[right]
    
    if current_fruit in fruit_count:
        fruit_count[current_fruit] += 1
    else:
        fruit_count[current_fruit] = 1
    
    while len(fruit_count) > 2:
        fruit_to_remove = fruit_num[left]
        fruit_count[fruit_to_remove] -= 1
        
        if fruit_count[fruit_to_remove] == 0:
            del fruit_count[fruit_to_remove]
            
        left += 1
    
    max_len = max(max_len, right - left + 1)

print(max_len)