from collections import deque

n, m = list(map(int, input().split()))

grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m + 1)] for _ in range(n + 1)]

cnt = 0


def in_range(x, y):
    return n > x >= 0 and m > y >= 0


def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and grid[x][y] == 1


def bfs():
    global cnt
    q = deque()
    q.append((0, 0))

    while q:
        x, y = q.popleft()

        dxs = [1, -1, 0, 0]
        dys = [0, 0, 1, -1]

        if x == n - 1 and y == m - 1:
            return grid[x][y]

        for dx, dy in zip(dxs, dys):
            nx, ny = dx + x, dy + y
            if can_go(nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny))
                grid[nx][ny] = grid[x][y] + 1

    return 0


ans = bfs()

print(ans)
