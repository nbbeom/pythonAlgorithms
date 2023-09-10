from collections import deque


def cal_dis(x, y, nx, ny):
    return abs(nx - x) + abs(ny - y)


def bfs():
    if cal_dis(home[0], home[1], festival[0], festival[1]) <= 1000:
        visited[n] = True
        return

    que = deque()
    # 집에서 갈수있는 모든 편의점을 큐에 담는다.
    for i in range(len(conv)):
        temp = cal_dis(home[0], home[1], conv[i][0], conv[i][1])
        if temp <= 1000:
            que.append(conv[i])
            visited[i] = True
    # 큐에 담긴 편의점에서 갈 수 있는 곳을 탐색한다.
    while que:
        cx, cy = que.popleft()
        for i in range(len(conv)):
            temp = cal_dis(cx, cy, conv[i][0], conv[i][1])
            if temp <= 1000 and not visited[i]:
                que.append(conv[i])
                visited[i] = True


t = int(input())

for _ in range(t):
    n = int(input())
    visited = [False] * (n + 1)
    home = [int(x) for x in input().split()]
    conv = []
    for j in range(n):
        x, y = map(int, input().split())
        conv.append([x, y])
    festival = [int(x) for x in input().split()]
    conv.append([x, y])

    bfs()
    # 마지막 지점을 festival 로 append 해서~ n인지점이 종점
    if visited[n] == True:
        print("happy")
    else:
        print("sad")
