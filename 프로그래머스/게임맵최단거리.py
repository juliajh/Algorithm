#

from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    answer = -1
    len_ = 1
    visited = [[False for i in range(m)] for j in range(n)]

    queue = deque([(0, 0, len_)])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    result = False
    while queue:
        x, y, len_ = queue.popleft()

        for i in range(0, 4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue

            if visited[nx][ny]:
                continue

            if maps[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny, len_ + 1))

                if nx == n - 1 and ny == m - 1:
                    answer = len_+1
                    result = True
                    break

        if result:
            break

    return answer
