n = int(input())


block = [int(input()) for _ in range(n)]

s1, e1 = list(map(int, input().split()))
s2, e2 = list(map(int, input().split()))


def remove_block(sp, ep, block):
    temp = []
    for i in range(len(block)):
        if ep - 1 < i or i < sp - 1:
            temp.append(block[i])
    return temp


temp = remove_block(s1, e1, block)
temp = remove_block(s2, e2, temp)


print(len(temp))
for t in temp:
    print(t)
