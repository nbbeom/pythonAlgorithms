n = int(input())
r1, c1, r2, c2 = list(map(int, input().split()))

from collections import deque

maxn = max(max(r1, r2), max(c1, c2))

grid = [[0 for _ in range(maxn + 1)] for _ in range(maxn + 1)]
visited = [[False for _ in range(maxn + 1)] for _ in range(maxn + 1)]


def in_range(x, y):
    return maxn >= x >= 0 and maxn >= y >= 0


def bfs():
    q = deque()
    q.append((r1, c1))

    while q:
        r, c = q.popleft()
        rs, cs = [-2, -2, 0, 0, 2, 2], [-1, 1, -2, 2, -1, 1]

        for rsx, csy in zip(rs, cs):
            nr, nc = r + rsx, csy + c
            if in_range(nr, nc) and not visited[nr][nc]:
                visited[nr][nc] = True
                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))


bfs()
if grid[r2][c2] == 0:
    print(-1)
else:
    print(grid[r2][c2])
