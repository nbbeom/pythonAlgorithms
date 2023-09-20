n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]


# 3x3 그래프의 금의 개수를 구한다.
def graph_3x3(x, y):
    temp = 0
    for i in range(3):
        for j in range(3):
            temp += graph[x + i][y + j]

    return temp


max_cnt = 0
x = 0
y = 0
# 격자 좌측 상단 모서리인 경우를 전부 탐색
for i in range(n - 2):
    for j in range(n - 2):
        temp_cnt = graph_3x3(x + i, y + j)
        max_cnt = max(max_cnt, temp_cnt)

print(max_cnt)
