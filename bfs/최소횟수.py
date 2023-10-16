import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())
visited_n = [False] * 200002
visited_p = [False] * 200002
visited_n[a], visited_p[a] = True, True
q = deque()
q.append((a, 0))
result = 0

while q:
    num, cnt = q.popleft()

    if num == b:
        result = cnt
        break

    if -200001 <= num * 2 <= 200001:
        if num * 2 < 0 and not visited_n[num * 2]:
            visited_n[num * 2] = True
            q.append((num * 2, cnt))
        elif num * 2 >= 0 and not visited_p[num * 2]:
            visited_p[num * 2] = True
            q.append((num * 2, cnt))
    if -200001 <= num - 1 <= 200001:
        # print(num-1, cnt)
        if num - 1 < 0 and not visited_n[num - 1]:
            visited_n[num - 1] = True
            q.append((num - 1, cnt + 1))
        elif num - 1 >= 0 and not visited_p[num - 1]:
            visited_p[num - 1] = True
            q.append((num - 1, cnt + 1))
    if -200001 <= num + 1 <= 200001:
        # print(num+1, cnt)
        if num + 1 < 0 and not visited_n[num + 1]:
            visited_n[num + 1] = True
            q.append((num + 1, cnt + 1))
        elif num + 1 >= 0 and not visited_p[num + 1]:
            visited_p[num + 1] = True
            q.append((num + 1, cnt + 1))

print(result)
