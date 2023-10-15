n = int(input())

grid = [list(map(int,input().split())) for _ in range(n)]

visited =[[False for _ in range(n+1)] for _ in range(n+1)] 
ans = []
ans_num = 0
def in_range(x,y):
    return n>x>=0 and n>y>=0

def can_go(x,y):
    return in_range(x,y) and not visited[x][y] 

def dfs(x,y):
    global ans_num
    dxs, dys = [0,0,1,-1], [1,-1,0,0]
    for dx,dy in zip(dxs,dys):
        nx, ny = dx+x,dy+y
        if can_go(nx,ny) and grid[nx][ny]==1 :
            visited[nx][ny] = True
            ans_num +=1
            dfs(nx,ny)
            
for i in range(n):
    for j in range(n):
        if not visited[i][j] and grid[i][j] == 1:
            ans_num+=1
            dfs(i,j)
            if ans_num != 0 :
                ans.append(ans_num)
                ans_num = 0

print(len(ans))
ans.sort()
for a in ans:
    if a-1 > 0 :
        print(a-1)
    else:
        print(a)