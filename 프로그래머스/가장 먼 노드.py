from collections import deque


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(len(edge)+1)]
    queue = deque()
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    queue.append(1)
    dist = [-1 for _ in range(len(edge)+1)]
    dist[1] = 0

    maxDist = 0
    count = 0
    while queue:
        start = queue.popleft()
        if maxDist < dist[start]:
            count = 1
            maxDist = dist[start]
        elif maxDist == dist[start]:
            count += 1
        for g in graph[start]:
            if dist[g] == -1:
                queue.append(g)
                dist[g] = dist[start]+1

    return count
