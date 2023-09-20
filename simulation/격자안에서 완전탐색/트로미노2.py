n, m = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]

# 가능한 모든 모양을 전부 적어줍니다.
shapes = [
    [[1, 1, 0], [1, 0, 0], [0, 0, 0]],
    [[1, 1, 0], [0, 1, 0], [0, 0, 0]],
    [[1, 0, 0], [1, 1, 0], [0, 0, 0]],
    [[0, 1, 0], [1, 1, 0], [0, 0, 0]],
    [[1, 1, 1], [0, 0, 0], [0, 0, 0]],
    [[1, 0, 0], [1, 0, 0], [1, 0, 0]],
]


def get_max_sum(x, y):
    max_sum = 0
    # 6개의 쉐입
    for i in range(6):
        is_posible = True
        sum_of_num = 0
        for dx in range(0, 3):
            for dy in range(0, 3):
                # 0 일때 통과
                if shapes[i][dx][dy] == 0:
                    continue
                if x + dx >= n or y + dy >= m:
                    is_posible = False
                else:
                    sum_of_num += grid[x + dx][y + dy]
        if is_posible:
            max_sum = max(max_sum, sum_of_num)

    return max_sum


ans = 0

for i in range(n):
    for j in range(m):
        ans = max(ans, get_max_sum(i, j))

print(ans)
