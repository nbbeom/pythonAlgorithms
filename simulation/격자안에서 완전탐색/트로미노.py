n, m = list(map(int, input().split()))

graph = [list(map(int, input().split())) for _ in range(n)]


max_num = 0


def straight(spx, spy):
    global max_num
    for i in range(3):
        max_x = 0
        max_y = 0
        for j in range(3):
            max_x += graph[spx + i][spy + j]
            max_y += graph[spx + j][spy + i]
        max_num = max(max_num, max_x, max_y)


def L_shpae1(spx, spy):
    global max_num
    dy = [1, -1]
    max_x = 0
    max_y = 0
    for j in range(2):
        max_x += graph[spy + j][spx]
        for y in dy:
            if y + spx > 0:
                max_y = max(graph[spy + j][y + spx], max_y)

    max_num = max(max_num, max_x + max_y)


def L_shpae2(spx, spy):
    global max_num
    dx = [1, -1]
    max_x = 0
    max_y = 0
    for i in range(2):
        max_y += graph[spy][spx + i]
        for x in dx:
            if x + spy > 0:
                max_x = max(graph[x + spy][spx + i], max_x)
    max_num = max(max_num, max_x + max_y)


for i in range(n):
    for j in range(m):
        if i + 2 < n and j + 2 < m:
            straight(i, j)
        if i + 1 < m and j + 1 < n:
            L_shpae1(i, j)
            L_shpae2(i, j)

print(max_num)
