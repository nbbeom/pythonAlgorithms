n = int(input())
visited = [False for _ in range(n+1)]
answer = []
print(visited      )
fin = []
def print_ans():
    for ele in answer:
         print(ele,end=" ")
    print()

def choose(curr_num):
    if curr_num == n+1:
        print_ans()
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
print(fin)