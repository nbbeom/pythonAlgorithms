from collections import deque

n = int(input())

r1, c1, r2, c2 = list(map(int, input().split()))
r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1


grid = [[0] * (n + 1) for _ in range(n + 1)]
visited = [[False for _ in range(n)] for _ in range(n)]
step = [  # step[i][j] : 시작점으로부터
    [0 for _ in range(n)] for _ in range(n)  # (i, j) 지점에 도달하기 위한  # 최단거리를 기록합니다.
]
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]


def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n and not visited[x][y]


def bfs(r, c):
    q = deque()
    q.append((r, c))
    while q:
        qr, qc = q.popleft()

        for dxs, dys in zip(dx, dy):
            nx = dxs + qr
            ny = dys + qc
            if in_range(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True
                # 거리가 1만큼 증가
                step[nx][ny] = step[qr][qc] + 1


bfs(r1, c1)

if step[r2][c2] == 0 and not n == 1:
    print("-1")
elif n == 1:
    print(0)
else:
    print(step[r2][c2])
