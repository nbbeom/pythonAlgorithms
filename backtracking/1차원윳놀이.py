n, m, k = list(map(int, input().split()))

turn = list(map(int, input().split()))

pieces = [1 for _ in range(k)]

dis_temp = 0
ans = 0
end_player = []


# 점수를 계산합니다.
def calc():
    score = 0
    for piece in pieces:
        if piece >= m:
            score += 1

    return score


def find_max(cnt):
    global ans

    # 말을 직접 n번 움직이지 않아도
    # 최대가 될 수 있으므로 항상 답을 갱신합니다.
    ans = max(ans, calc())

    # 더 이상 움직일 수 없으면 종료합니다.
    if cnt == n:
        return

    for i in range(k):
        # 움직여서 더 이득이 되지 않는
        if pieces[i] >= m:
            continue

        pieces[i] += turn[cnt]
        find_max(cnt + 1)
        pieces[i] -= turn[cnt]


find_max(0)
print(ans)
