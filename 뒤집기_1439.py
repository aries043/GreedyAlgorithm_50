import sys

numbers = sys.stdin.readline()
ans = 0
cnt_ten = numbers.count('10')
cnt_one = numbers.count('01')

if cnt_ten == 0:
    if cnt_one != 0:
        ans = 1
else:
    if cnt_ten > cnt_one:
        ans = cnt_ten
    else:
        ans = cnt_one

print(ans)

010101010