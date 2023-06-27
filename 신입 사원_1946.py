import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    ans = 1
    people = [0 for _ in range(N)]
    
    for _ in range(N):
        doc, inv = map(int, sys.stdin.readline().split())
        people[doc-1] = inv

    minMan = people[0]
    for i in range(0, N):
        if minMan > people[i]:
            ans += 1
            minMan = people[i]
            
    
    print(ans)