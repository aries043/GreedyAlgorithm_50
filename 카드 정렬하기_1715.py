from heapq import heapify, heappop, heappush

N = int(input())
cards = []
for _ in range(N):
    cards.append(int(input()))

heapify(cards)

ans = 0

for i in range(N-1):
    tmp1 = heappop(cards)
    tmp2 = heappop(cards)
    ans += tmp1 + tmp2
    heappush(cards, tmp1 + tmp2)

print(ans)