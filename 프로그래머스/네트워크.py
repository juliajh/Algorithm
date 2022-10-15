def dfs(root, visited, computers):
    visited[root] = True
    for a, b in enumerate(computers[root]):
        if b == 1 and not visited[a]:
            dfs(a, visited, computers)


def solution(n, computers):
    answer = 0
    visited = [False]*n
    for i in range(n):
        if not visited[i]:
            dfs(i, visited, computers)
            answer += 1
    return answer
