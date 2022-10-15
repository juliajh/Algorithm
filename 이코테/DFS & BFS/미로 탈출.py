from collections import deque
import queue

n, m = map(int, input().splilt())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx, ny))

    return graph[n-1][m-1]
