# 수평 두칸 수직 한칸
# 수직 두칸 수평 한칸

import sys
input = sys.stdin.readline

inp = input()

dx = [-2, -2, -1, 1, 2, 2, -1, 1]
dy = [-1, 1, 2, 2, -1, 1, -2, -2]

x = 0
y = int(inp[1])

if inp[0] == 'a':
    x = 1
elif inp[0] == 'b':
    x = 2
elif inp[0] == 'c':
    x = 3
elif inp[0] == 'd':
    x = 4
elif inp[0] == 'e':
    x = 5
elif inp[0] == 'f':
    x = 6
elif inp[0] == 'g':
    x = 7
elif inp[0] == 'e':
    x = 8

count = 0
for i in range(8):
    nx = x+dx[i]
    ny = y+dy[i]

    if nx > 8 or ny > 8 or nx < 1 or ny < 1:
        continue

    count += 1

print(count)
