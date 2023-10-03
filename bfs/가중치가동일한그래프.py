import sys

# recursion의 최대 깊이(N*M)인 10000으로 설정해줍니다.
sys.setrecursionlimit(10000)

INT_MAX = sys.maxsize

# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))

a = [list(map(int, input().split())) for _ in range(n)]

# backtracking에 필요한 변수들 입니다.
visited = [[False for _ in range(m)] for _ in range(n)]

ans = INT_MAX


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m


# 격자를 벗어나지 않으면서, 뱀도 없고, 아직 방문한 적이 없는 곳이라면
# 이동이 가능합니다.
def can_go(x, y):
    return in_range(x, y) and a[x][y] and not visited[x][y]


# backtracking을 통해 최소 이동 횟수를 구합니다.
def find_min(x, y, cnt):
    global ans

    if x == n - 1 and y == m - 1:
        ans = min(ans, cnt)
        return

    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    # 현재 위치를 기준으로 4방향을 확인해봅니다.
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        # 아직 방문한 적이 없으면서 갈 수 있는 곳이라면
        # 더 진행해봅니다.
        if can_go(new_x, new_y):
            # 지금까지의 선택이 최단경로 로서 부적합했을 수 있으므로
            # 퇴각시 visited값을 다시 false로 바꿔
            # 다른 방향으로 진행할때도 기회를 주어 모든 가능한
            # 경로를 전부 탐색할 수 있도록 합니다.
            visited[new_x][new_y] = True
            find_min(new_x, new_y, cnt + 1)
            visited[new_x][new_y] = False


# 현재까지 이동 횟수가 0일때, (0, 0)에서 시작하는
# 재귀를 호출합니다.
find_min(0, 0, 0)

# 불가능한 경우라면 -1을 답으로 넣어줍니다.
if ans == INT_MAX:
    ans = -1

print(ans)
