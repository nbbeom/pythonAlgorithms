n,r,c = list(map(int,input().split()))

grid = [
    list(map(int,input().split()))
    for _ in range(n)    
]

ans = []

ans.append(grid[r-1][c-1])
max_num = grid[r-1][c-1]
max_x  , max_y = r-1, c-1

def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<n

def simulate(x,y):
    global max_num
    global max_x,max_y
    dxs ,dys =[1,-1,0,0] , [0,0,1,-1]

    for dx, dy in zip(dxs,dys):
        nx ,ny = dx+x, dy+y
        
        if in_range(nx,ny) and max_num < grid[nx][ny] :
            max_num = grid[nx][ny]
            max_y = ny
            max_x = nx
            ans.append(grid[max_x][max_y])
            break;
    
            
for _ in range(n*n):
    simulate(max_x,max_y)

for a in ans :
    print(a, end= " ")