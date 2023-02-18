cnt = []
ans = int(input())
if ans%10!=0:
    print("-1")
else:
    k = 0
    while(ans>=300):
        ans -= 300
        k += 1
    cnt.append(k)
    k = 0
    while(ans>=60):
        ans -= 60
        k += 1
    cnt.append(k)
    k = 0
    while(ans>=10):
        ans -= 10
        k += 1
    cnt.append(k)
    for i in range(3):
        print(cnt[i], end=" ")
