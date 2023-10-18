from collections import deque

n, k = list(map(int, input().split()))

visited_teleport = [False for _ in range(100000)]


def bfs():
    q = deque()
    q.append((n, 0))

    while q:
        x, cnt = q.popleft()
        if x == k:
            return cnt
        for next_n in (x - 1, x + 1, 2 * x):
            if 0 <= next_n < 100001 and not visited_teleport[next_n]:
                visited_teleport[next_n] = True
                q.append((next_n, cnt + 1))


print(bfs())
