import sys

sys.setrecursionlimit(2500)
n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def can_go(x, y, value):
    return in_range(x, y) and not visited[x][y] and array[x][y] == value


def dfs(x, y, value):
    global areaCnt
    visited[x][y] = True
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny, value):
            dfs(nx, ny, value)
            areaCnt += 1


answer = []
bomb = 0
for i in range(n):
    for j in range(n):
        if can_go(i, j, array[i][j]):
            areaCnt = 1
            dfs(i, j, array[i][j])
            answer.append(areaCnt)
            if areaCnt >= 4:
                bomb += 1
answer = sorted(answer)
print(bomb, answer[-1])
