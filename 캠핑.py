count = 0
while(1):
    ans = 0
    count += 1
    L, P, V = map(int, input().split())
    if (L+P+V)==0:
        break
    while(1):
        if V-P>=0:
            V -= P
            ans += L
        else:
            if V > L:
                ans += L
                break
            else:
                ans += V
                break
    print("Case %d: %d" %(count, ans))
