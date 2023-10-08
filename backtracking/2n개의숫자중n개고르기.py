import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력:

n = int(input())
num = list(map(int, input().split()))

ans = INT_MAX


def find_min(idx, cnt, diff):
    global ans
    
    if idx == 2 * n:
        if cnt == n:
            ans = min(ans, abs(diff))
        return
    
    # 현재 숫자를 첫 번째 그룹에 사용한 경우입니다.
    find_min(idx + 1, cnt + 1, diff + num[idx])
    # 현재 숫자를 두 번째 그룹에 사용한 경우입니다.
    find_min(idx + 1, cnt, diff - num[idx])
    

find_min(0, 0, 0)
print(ans)