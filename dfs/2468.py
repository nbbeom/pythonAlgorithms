import sys

sys.setrecursionlimit(100000)
n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False for _ in range(n + 1)] for _ in range(n + 1)]
cnt = 0
ans = 0
precipitation = 0


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def is_water(x, y):
    global precipitation
    return in_range(x, y) and grid[x][y] > precipitation


def dfs(x, y):
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    for dxs, dys in zip(dx, dy):
        nx, ny = dxs + x, dys + y
        if is_water(nx, ny) and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny)


for k in range(1, max(map(max, grid))):
    visited = [[False] * (n + 1) for _ in range(n + 1)]
    cnt = 0
    safe_zone = 0
    precipitation = k
    for i in range(n):
        for j in range(n):
            if is_water(i, j) and not visited[i][j]:
                visited[i][j] = True
                dfs(i, j)
                cnt += 1

    ans = max(ans, cnt)

print(ans)
