from collections import deque

n = int(input())
graph = []
num = []

for i in range(n):
    graph.append(list(map(int, input())))

visited = [[False] * n for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    if graph[x][y] == 0 or visited[x][y]:  # 그래프가  0 or 방문한 곳
        return
    queue = deque([(x, y)])
    visited[x][y] = True  # 방문처리
    temp = 0
    while queue:
        x, y = queue.popleft()
        temp += 1  # 방문지가 있는경우
        for i in range(4):  # 4방향 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < n
                and 0 <= ny < n
                and not visited[nx][ny]
                and graph[nx][ny] == 1
            ):
                queue.append((nx, ny))
                visited[nx][ny] = True
    num.append(temp)


for i in range(n):
    for j in range(n):
        bfs(i, j)  # 방문지 찾기

print(len(num))
num.sort()
for i in num:
    print(i)
