n = int(input())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def in_range(x, y):
    return x >= 0 and y >= 0 and x < n and y < n


def can_move(x, y):
    if not in_range(x, y):
        return False

    if grid[x][y] == 1 and not visited[x][y]:
        return True
    else:
        return False


def dfs(x, y):
    global cnt
    for i in range(4):
        if can_move(x + dx[i], y + dy[i]):
            visited[x + dx[i]][y + dy[i]] = True
            cnt += 1
            dfs(x + dx[i], y + dy[i])


grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]


answer = []
cnt = 0

for i in range(n):
    for j in range(n):
        if can_move(i, j):
            visited[i][j] = True
            cnt = 1
            dfs(i, j)
            answer.append(cnt)

answer.sort()
print(len(answer))
for ans in answer:
    print(ans)
