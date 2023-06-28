import sys

N = int(sys.stdin.readline().rstrip())
chars = [0 for _ in range(26)]
ans = 0

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    digit = 1
    for ch in reversed(word):
        chars[ord(ch)-65] += 1 * digit
        digit *= 10

value = 9

for ch in sorted(chars, reverse=True):
    if ch != 0:
        ans += ch*value
        value -= 1
print(chars)
print(ans)