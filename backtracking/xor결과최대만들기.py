import functools

# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
a = list(map(int, input().split()))

ans = 0


def find_max_xor(curr_idx, cnt, curr_val):
    global ans

    if cnt == m:
        ans = max(ans, curr_val)
        return

    if curr_idx == n:
        return

    # curr_idx index에 있는 숫자를 선택하지 않은 경우
    find_max_xor(curr_idx + 1, cnt, curr_val)

    # curr_idx index에 있는 숫자를 선택한 경우
    find_max_xor(curr_idx + 1, cnt + 1, curr_val ^ a[curr_idx])


find_max_xor(0, 0, 0)

print(ans)
