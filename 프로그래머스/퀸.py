# 다시

def solution(n):
    answer = 0
    place = [[False for i in range(n)] for j in range(n)]

    def dfs(x, y, count):
        if count == n:
            return True
        for i in range(4):
            if place[nx][ny]:
                continue
            place[nx][ny] = True
            count += 1
            dfs(nx, ny, count)
        return False

    for i in range(n):
        for j in range(n):
            if dfs(i, j, 0):
                answer += 1
    return answer


print(solution(4))
