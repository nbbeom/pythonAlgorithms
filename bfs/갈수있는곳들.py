from collections import deque

n, k = list(map(int, input().split()))

graph = [list(map(int, input().split())) for _ in range(n)]
sp = [list(map(int, input().split())) for _ in range(k)]
visited = [[False] * n for _ in range(n)]
count = 0


def in_range(x, y):
    return n > x >= 0 and n > y >= 0


def can_go(x, y):
    return not visited[x][y] and graph[x][y] == 0


def bfs(x, y):
    q = deque()
    q.append((x, y))
    global count
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        qx, qy = q.popleft()
        for dxs, dys in zip(dx, dy):
            nx = dxs + qx
            ny = dys + qy
            if in_range(nx, ny) and can_go(nx, ny):
                visited[nx][ny] = True
                count += 1
                q.append((nx, ny))


for s in sp:
    nx = s[0] - 1
    ny = s[1] - 1
    if in_range(nx, ny) and can_go(nx, ny):
        visited[nx][ny] = True
        count += 1
        bfs(nx, ny)

print(count)
