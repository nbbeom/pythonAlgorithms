# 인접행렬 : 인접 행렬을 활용하여 탐색할경우 각 정점에대해 나머지 정점에 연결된
# 간선이 있는지 여부를 n 번확인하여 탐색 간선의 수 가 적을때 비효율적임
# (O(n^2))
def dfs(v):
    for curr_v in range(1, n + 1):
        if graph[v][curr_v] == 1 and not visited[curr_v]:
            visited[curr_v] = True
            global count
            count += 1
            dfs(curr_v)


n, m = map(int, input().split())
count = 0
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1

visited[1] = True
dfs(1)

print(count)


# 인접 리스트 : 전반적인 알고리즘은 동일
# 간선이 존재할 때만 배열에 추가해 주기 때문에 메모리 누수 방지
# 탐색시 불필요한 탐색 연산을 줄임
# (O(n+m))


def dfs(v):
    # 해당 정점에 이어져 있는 모든 정점을 탐색
    for curr_v in graph[v]:
        # 아직 간선이 존재하고 방문한 적이 없는 정점에 대해 탐색
        if not visited[curr_v]:
            visited[curr_v] = True
            global count
            count += 1
            dfs(curr_v)


n, m = tuple(map(int, input().split()))
count = 0
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = tuple(map(int, input().split()))
    graph[v1].append(v2)
    graph[v2].append(v1)


visited[1] = True
dfs(1)

print(count)
