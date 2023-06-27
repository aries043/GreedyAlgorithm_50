import sys

A, B = map(int, sys.stdin.readline().split())
ans = 1

while(A!=B):
    print(A, B)
    if A > B:
        ans = -1
        break
    elif B%10==1:
        ans += 1
        B = (B-1)//10
    elif B%2==0:
        ans += 1
        B = B//2
    else:
        ans = -1
        break

print(ans)