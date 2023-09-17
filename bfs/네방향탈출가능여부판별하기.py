from collections import deque

n , m = list(map(int, input().split()))

graph = [list(map(int,input().split())) for _ in range(m)]
visited = [[False] * n for _ in range(m)]

def in_range(x,y):
    return n > x >= 0 and m > y >= 0
def can_go(x,y):
    return not visited[x][y] and graph[x][y] == 1

def bfs(x,y):
    q = deque()
    q.append((x,y))
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    while q:
        qx,qy = q.popleft()

        for ndx ,ndy in zip(dx,dy):
            nx = ndx+ qx
            ny = ndy+ qy
            if in_range(nx,ny) and can_go(nx,ny):
                visited[nx][ny] = True
                q.append((nx,ny))
                if nx == n-1 and ny == m-1:
                    return 1
    
    return 0

visited[0][0] =True
print(bfs(0,0))

        
        