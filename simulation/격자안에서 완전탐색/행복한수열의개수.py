n, m = list(map(int, input().split()))

grid = [list(map(int, input().split())) for _ in range(n)]

seq = [[0] for _ in range(n)]


def is_happy_seq(seq):
    cnt = 1
    max_ccnt = 1
    for i in range(1, len(seq)):
        if seq[i - 1] == seq[i]:
            cnt += 1
        else:
            cnt = 1
        max_ccnt = max(max_ccnt, cnt)

    return max_ccnt >= m


total_count = 0

for i in range(0, n):
    seq = grid[i][:]
    if is_happy_seq(seq):
        total_count += 1

for i in range(0, n):
    seq = []
    for j in range(0, n):
        seq.append(grid[j][i])
    if is_happy_seq(seq):
        total_count += 1

print(total_count)
