# 변수선언
n = 5
gird = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
]


# row 형의 cos_s ~col_e 사이의 금의 개수를 계산
def get_num_of_gold(row, col_s, col_e):
    num_of_gold = 0
    # 1*3 격자가 n*n 격자를 벗어나는 경우는 계산하지 않습니다.
    for col in range(col_s, col_e + 1):
        num_of_gold += grid[row][col]

    return num_of_gold


max_gold = 0

# (row, col)이 1 * 3 격자의 좌측 모서리인 경우를 전부 탐색합니다.
for row in range(n):
    for col in range(n):
        if col + 2 >= n:
            continue
        # 금의 개수를 계산합니다.
        num_of_gold = get_num_of_gold(row, col, col + 2)
        # 최대 금의 개수를 저장합니다.
        max_gold = max(max_gold, num_of_gold)

print(max_gold)
