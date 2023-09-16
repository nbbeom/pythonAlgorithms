n, m = list(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
answer = list()


def in_range(x, y):
    return x >= 0 and y >= 0 and x < n and y < m


def can_go(x, y, k):
    if in_range(x, y):
        if grid[x][y] > k and not visited[x][y]:
            return True
    return False


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

visited = [[False] * m for _ in range(n)]


def dfs(x, y, k):
    global cnt
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if can_go(new_x, new_y, k):
            visited[new_x][new_y] = True
            cnt += 1
            dfs(new_x, new_y, k)


cnt = 0
safe_zone = 0
height = []
for k in range(1, max(map(max, grid))):
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    safe_zone = 0
    for i in range(n):
        for j in range(m):
            if can_go(i, j, k):
                visited[i][j] = True
                dfs(i, j, k)
                if cnt > 0:
                    safe_zone += 1
    if safe_zone != 0:
        height.append(k)
        answer.append(safe_zone)


# 안전영역 높이 K 안전영역 수
if len(answer) != 0:
    print(str(height[answer.index(max(answer))]) + " " + str(max(answer)))
else:
    print(str(min(map(min, grid))) + " " + "0")
