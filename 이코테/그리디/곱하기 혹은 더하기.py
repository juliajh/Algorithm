import sys

input = sys.stdin.readline
S = input().strip()
final = int(S[0])

for letter in S:
    num = int(letter)
    if (num <= 1 or final <= 1):
        final = final+num
    else:
        final = final*num

print(final)
