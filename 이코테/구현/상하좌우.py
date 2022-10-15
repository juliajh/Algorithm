import sys

input = sys.stdin.readline

N = int(input())
plans = list(input().split())

# 동 북 서 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
direction = ['R', 'U', 'L', 'D']
x, y = 1, 1


for plan in plans:
    for i in range(len(direction)):
        if plan == direction[i]:
            nx = x+dx[i]
            ny = y+dy[i]

    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue

    x = nx
    y = ny
print(x, y)
