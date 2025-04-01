import sys, math
read = sys.stdin.readline
INF = float('inf')

N = int(read())
x_dict, x_list, reg = dict(), set(), list()

for _ in range(N):
    x1, x2, y1, y2 = map(int, read().split())
    reg.append((y1, x1, x2, 1)), reg.append((y2, x1, x2, -1))
    x_list.add(x1), x_list.add(x2)
    
reg.sort()
x_list = sorted(x_list)
nx = len(x_list)
n = 2 ** math.ceil(math.log2(nx - 1))
tree, count = [0] * (2 * n), [0] * (2 * n)

for i in range(nx):
    x_dict[x_list[i]] = i

def update(flag, x1, x2, pos = 1, left = 0, right = n - 1):
    
    mid = (left + right) // 2
    
    if x1 > right or x2 <= left:
        return
    
    elif x1 <= left and x2 > right:
        count[pos] += flag
        
    else:
        if x1 <= mid:
            update(flag, x1, x2, pos*2, left, mid)
        if mid + 1 < x2:
            update(flag, x1, x2, pos*2+1, mid+1, right)
            
    if count[pos] != 0:
        tree[pos] = x_list[right + 1] - x_list[left]
        
    elif left == right:
        tree[pos] = 0
        
    else:
        tree[pos] = tree[pos*2] + tree[pos*2+1]
        
    return

ans = 0
p_y = reg[0][0]

for y, x1, x2, flag in reg:
    if y > p_y:
        ans += tree[1] * (y - p_y)
    update(flag, x_dict[x1], x_dict[x2])
    p_y = y
    
print(ans)