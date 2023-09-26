import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력:
n = int(input())
num = list(map(int, input().split()))

ans = INT_MAX


def find_min(idx, cnt):
    global ans

    # 마지막 위치를 넘었을 때
    # 그 중 최소 이동 횟수를 갱신합니다.
    if idx >= n - 1:
        ans = min(ans, cnt)
        return

    for dist in range(1, num[idx] + 1):
        find_min(idx + dist, cnt + 1)


find_min(0, 0)

if ans == INT_MAX:
    ans = -1

print(ans)
