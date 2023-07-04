import sys
from heapq import heappush, heappop

N, K = map(int, sys.stdin.readline().split())

ans = 0
jewels = []
bags =[]

for _ in range(N):
    M, V = map(int, sys.stdin.readline().split())
    heappush(jewels, (M, V))

for _ in range(K):
    K = int(sys.stdin.readline())
    bags.append(K)
bags.sort()

can = []
for bag in bags:
    while jewels and bag >= jewels[0][0]:
        heappush(can, -heappop(jewels)[1])
    if can:
        ans -= heappop(can)
    elif not jewels:
        break
    
print(ans)