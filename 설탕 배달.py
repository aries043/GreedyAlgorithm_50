N = int(input())
ans = 0

if N<=4:
    print("-1")
else:
    while(N>=5):
        N-=5
        ans+=1

    while(N>=3):
        N-=3
        ans+=1
    print(ans+N)
