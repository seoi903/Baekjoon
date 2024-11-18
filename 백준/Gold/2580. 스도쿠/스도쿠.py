import sys
from collections import deque


def sol():
    while coordinate:
        y, x = coordinate.popleft()
        # candidate = candidate_dict.get((y, x), check_row(*check_col(*check_area(y, x))))
        if (y, x) not in candidate_dict:
            candidate = check_area(y, x)
            candidate = check_col(candidate, y, x)
            candidate = check_row(candidate, y, x)
            candidate_dict[(y, x)] = candidate
        candidate = candidate_dict[(y, x)]
        for i in candidate:
            if i > maps[y][x]:
                maps[y][x] = i
                before.append((y, x))
                break
        else:
            coordinate.appendleft((y, x))
            maps[y][x] = 0
            candidate_dict.pop((y, x))
            coordinate.appendleft(before.pop())
    for m in maps:
        print(*m, sep=' ')


def check_area(y, x):
    c_y = (y // 3) * 3
    c_x = (x // 3) * 3
    candidate = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(c_y, c_y + 3):
        for j in range(c_x, c_x + 3):
            if maps[i][j] in candidate:
                candidate.remove(maps[i][j])
    # print(candidate)
    return candidate


def check_col(candidate, y, x):
    for m in maps:
        if m[x] in candidate:
            candidate.remove(m[x])
    return candidate


def check_row(candidate, y, x):
    for m in maps[y]:
        if m in candidate:
            candidate.remove(m)
    return candidate


if __name__ == "__main__":
    maps = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
    coordinate = deque()        # 들어가야 하는 좌표들
    before = deque()        # 이미 값이 할당되었던 좌표들
    for i in range(9):
        for j in range(9):
            if maps[i][j] == 0:
                coordinate.append((i, j))
    candidate_dict = dict()
    sol()