N = int(input())
ans = 0
five = N//5

while(five>=0):
    if (N - 5*five)%3==0:
        ans = five + (N - 5*five)//3
        break
    else:
        five -= 1

print(ans) if ans != 0 else print(-1)
