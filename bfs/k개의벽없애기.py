import sys
from collections import deque

INT_MAX = sys.maxsize

# 변수 선언 및 입력
n, k = tuple(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]

r1, c1 = tuple(map(int, input().split()))
r2, c2 = tuple(map(int, input().split()))
r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1

stone_pos = [(i, j) for i in range(n) for j in range(n) if a[i][j]]

# bfs에 필요한 변수들 입니다.
q = deque()
visited = [[False for _ in range(n)] for _ in range(n)]
step = [  # step[i][j] : 시작점으로부터
    [0 for _ in range(n)] for _ in range(n)  # (i, j) 지점에 도달하기 위한  # 최단거리를 기록합니다.
]

ans = INT_MAX


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def can_go(x, y):
    return in_range(x, y) and not a[x][y] and not visited[x][y]


# queue에 새로운 위치를 추가
# 방문 여부를 표시.
def push(nx, ny, new_step):
    q.append((nx, ny))
    visited[nx][ny] = True
    step[nx][ny] = new_step


def bfs():
    while q:
        x, y = q.popleft()

        dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                push(nx, ny, step[x][y] + 1)

    # 답을 갱신
    if visited[r2][c2]:
        return step[r2][c2]
    else:
        return INT_MAX


def find_min(idx, cnt):
    global ans

    if idx == len(stone_pos):
        if cnt == k:
            # visited, step 값을 초기화
            for i in range(n):
                for j in range(n):
                    visited[i][j] = False
                    step[i][j] = 0

            # bfs를 이용해 최소 이동 횟수
            push(r1, c1, 0)
            min_dist = bfs()
            ans = min(ans, min_dist)

        return

    x, y = stone_pos[idx]
    a[x][y] = 0
    find_min(idx + 1, cnt + 1)
    a[x][y] = 1

    find_min(idx + 1, cnt)


find_min(0, 0)

if ans == INT_MAX:  # 불가능한 경우라면
    ans = -1  # -1을 답으로 넣어줍니다.

print(ans)
