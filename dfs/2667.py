n = int(input())
graph = []
num = []

for i in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0  # 방문처리
        global temp
        temp += 1  # 방의 개수
    else:
        return False

    for i in range(4):
        dfs(x + dx[i], y + dy[i])  # 4방향 탐색

    return True


temp = 0

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            num.append(temp)  # 방의 사이즈를 num에 추가
            temp = 0

print(len(num))
num.sort()
for i in num:
    print(i)
