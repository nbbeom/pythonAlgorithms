n, t = list(map(int, input().split()))

grid = [list(map(int, input().split())) for _ in range(2)]
grid = sum(grid, [])

for i in range(t):
    next_grid = []
    temp = grid[-1]
    for j in range(n * 2 - 1):
        next_grid.append(grid[j])
    next_grid.insert(0, temp)
    grid = next_grid

print(grid)
