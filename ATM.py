import heapq

N = int(input())
fans = list(map(int, input().split()))
ans_arr = []
sum_time = 0
ans = 0

for time in fans:
    heapq.heappush(ans_arr, time)

for _ in range(N):
    sum_time += heapq.heappop(ans_arr)
    ans += sum_time

print(ans)
