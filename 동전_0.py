import heapq

N, K= map(int, input().split())
money = []
ans = 0

for _ in range(N):
    won = int(input())
    if won<=K:
        heapq.heappush(money, (-won, won))

while money:
    won = heapq.heappop(money)[1]
    tmp = K//won
    K -= won*tmp
    ans += tmp

print(ans)
