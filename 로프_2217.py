N = int(input())
ans = []
ropes = []

for _ in range(N):
    ropes.append(int(input()))

ropes.sort()

for rope in ropes:
    ans.append(N*rope)
    N -= 1

print(max(ans))