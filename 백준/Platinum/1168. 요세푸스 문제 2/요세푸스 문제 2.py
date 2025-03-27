from sys import stdin

input = stdin.readline

def init(tree, node, start, end):
    if start==end:
        tree[node] = 1
        return tree[node]
    mid = (start+end)//2
    tree[node] = init(tree, node*2,start, mid) + init(tree, node*2+1, mid+1, end)
    return tree[node]

def update(tree, node, start, end, dellete):
    tree[node] -=1
    if start==end:
        return 0

    else:
        mid = (start+end)//2
        if dellete<=mid:
            return update(tree, node*2, start, mid,dellete)
        else:
            return update(tree, node*2+1, mid+1, end, dellete)

def query(tree, node, start, end, order):
    if start==end:
        return start
    
    mid = (start + end)//2

    if order <= tree[node*2]:
        return query(tree, node*2, start, mid, order)
    else:
        return query(tree, node*2+1, mid+1, end, order-tree[node*2])
    
n, k = map(int,input().split())
tree = [0]*3000000

init(tree,1, 1, n) 
index = 1

array = list()

for i in range(n):
    
    size = n-i
    index += k-1

    if index%size == 0:
        index = size
    elif index>size: 
        index %= size

    num = query(tree, 1, 1, n, index)

    update(tree, 1, 1, n, num)
    array.append(str(num))

print("<",", ".join(array),">",sep='')