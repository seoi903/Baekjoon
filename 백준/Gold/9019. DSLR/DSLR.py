from collections import deque

def oper_D(n):
	res = n * 2
	if res > 9999:
		res %= 10000
	return res
def oper_S(n):
	res = n
	if res == 0 : return 9999
	res -= 1
	return res
def oper_L(n):
	front = n % 1000
	back = n // 1000
	res = front * 10 + back 
	return res
def oper_R(n):
	front = n % 10
	back = n // 10
	res = front * 1000 + back
	return res 
def go(s, t):
	queue = deque()
	visited = set()
	queue.append((s, ""))
	visited.add(s)
	while queue:
		cur_num, oper = queue.popleft()
		if cur_num == t:
			print(oper)
			return
		tmp = oper_D(cur_num)
		if tmp not in visited:
			visited.add(tmp)
			queue.append((tmp, oper+"D"))
		
		tmp = oper_S(cur_num)
		if tmp not in visited:
		    visited.add(tmp)
		    queue.append((tmp, oper+"S"))
		    
		tmp = oper_L(cur_num)
		if tmp not in visited:
		    visited.add(tmp)
		    queue.append((tmp, oper+"L"))
		
		tmp = oper_R(cur_num)
		if tmp not in visited:
		    visited.add(tmp)
		    queue.append((tmp, oper+"R"))
		
T = int(input())
for _ in range(T):
    start, target = map(int, input().split())
    go(start, target)