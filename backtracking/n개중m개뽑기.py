n,m = tuple(map(int,input().split()))

ans =[]
visited = [False for _ in range(n+1)]

def print_combination():
    for e in ans:
        print(e, end=" ")
    print()


def dfs(curr_num, cnt):
    if curr_num == n+1:
        if cnt == m:
            print_combination()
        return

    ans.append(curr_num)
    dfs(curr_num+1,cnt+1)
    ans.pop()

    dfs(curr_num+1,cnt)

    return

dfs(1,0)            