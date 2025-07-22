import sys
input = sys.stdin.readline

def ccw(x1,y1,x2,y2,x3,y3):
    return (x2-x1)*(y3-y2) - (x3-x2)*(y2-y1)

def intersect(x1,y1,x2,y2,x3,y3,x4,y4):
    a = ccw(x1,y1,x2,y2,x3,y3)
    b = ccw(x1,y1,x2,y2,x4,y4)
    c = ccw(x3,y3,x4,y4,x1,y1)
    d = ccw(x3,y3,x4,y4,x2,y2)
    if a==b==c==d==0:
        return not (max(x1,x2)<min(x3,x4) or max(x3,x4)<min(x1,x2) or
                    max(y1,y2)<min(y3,y4) or max(y3,y4)<min(y1,y2))
    return (a*b <= 0 and c*d <= 0)

n = int(input())
poly = [tuple(map(int,input().split())) for _ in range(n)]
poly.append(poly[0])

for _ in range(3):
    x,y = map(int,input().split())
    # 경계 위에 있는지 확인
    on_edge = False
    for (x1,y1),(x2,y2) in zip(poly, poly[1:]):
        if ccw(x,y,x1,y1,x2,y2)==0:
            if min(x1,x2) <= x <= max(x1,x2) and min(y1,y2) <= y <= max(y1,y2):
                print(1)
                on_edge = True
                break
    if on_edge: continue

    # 반직선 교차 수 세기
    zx, zy = x+1, y + 1_000_000_001
    cnt = 0
    for (x1,y1),(x2,y2) in zip(poly, poly[1:]):
        if intersect(x, y, zx, zy, x1, y1, x2, y2):
            cnt += 1
    print(cnt % 2)