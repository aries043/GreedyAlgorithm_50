N = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))
ans = 0
del costs[N-1]


minCost = costs[0]
tmp = 0

for road, cost in zip(roads, costs):
    if cost < minCost:
        ans += tmp*minCost
        tmp = road
        minCost = cost
    else:
        tmp += road
    
ans += minCost * tmp
print(ans)