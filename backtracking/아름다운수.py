n = int(input())

ans = 0
seq =list()

def is_beautiful():
    i = 0

    while i < n:
        #연속하여 해당 숫자만큼 나오는지 check
        if i + seq[i] -1 >=n:
            return False
        
        #연속해서 해당 숫자가 있는지 check
        for j in range(i, i+seq[i]):
            if seq[j] != seq[i]:
                return False
        
        i += seq[i]
    
    return True

def count_beautiful_seq(cnt):
    global ans

    # 재귀 탈출 조건
    if cnt == n:
        if is_beautiful():
            ans+=1
        return
    
    # 재귀 별로 새로 아름다운 수를 만든다
    for i in range(1,5):
        seq.append(i)
        count_beautiful_seq(cnt+1)
        seq.pop()
            

count_beautiful_seq(0)   
print(ans) 