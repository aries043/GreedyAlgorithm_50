N = input()

if '0' not in N:
    print(-1)

else:
    a = []
    for i in N:
        a.append(int(i))

    a.remove(0)

    if sum(a)%3!=0:
        print(-1)
        
    else:
        a.sort(reverse=True)
        a.append(0)
        print(''.join(str(s) for s in a))