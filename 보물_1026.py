import copy

aArray = []
bArray = []

sum = 0

N = int(input())
aArray = list(map(int, input().split()))
bArray = list(map(int, input().split()))

for i in range(N):
    maxB = max(bArray)
    minA = min(aArray)
    sum += minA * maxB
    del bArray[bArray.index(maxB)]
    del aArray[aArray.index(minA)]

print(sum)
    