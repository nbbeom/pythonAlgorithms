n = int(input())
visited = [False for _ in range(n+1)]
answer = []
fin_answer = []
print(visited)
def print_ans():
    for i in range(len(fin_answer)-1, -1,-1):
        for ans in fin_answer[i]:
            print(ans, end=" ")
        print()

def choose(curr_num):
    if curr_num == n+1:
        temp = []
        for e in answer:
            temp.append(e)
        fin_answer.append(temp)
        return
    
    for i in range(1,n+1):
        if visited[i]:
            continue

        visited[i] = True
        answer.append(i)
        choose(curr_num+1)
        answer.pop()
        visited[i]= False

choose(1)
print_ans()