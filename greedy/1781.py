from heapq import heappush
from heapq import heappop

n = int(input())
arrays = []
for i in range(n):
    dead,array = map(int, input().split())
    arrays.append((dead,array))

arrays.sort()

queue = []
# print(arrays)
for i in arrays:
    heappush(queue,i[1])
    if(i[0]<len(queue)):
        heappop(queue)
    # print(queue)

print(sum(queue))