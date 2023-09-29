n = int(input())

grid = [list(map(int,input().split())) for _ in range(n)]
choose_list =[]
visisted = [False for _ in range(n) ]
ans = []

def choose(curr_idx):
    if curr_idx == n:
        choose_value = 0
        for k in choose_list:
           choose_value+=k 
        ans.append(choose_value)  
        return
    
    for i in range(n):
        if not visisted[i]:
            visisted[i] =True
            choose_list.append(grid[curr_idx][i])
            choose(curr_idx+1)
            choose_list.pop()
            visisted[i] = False

choose(0)
print(max(ans))