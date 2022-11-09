from collections import deque


def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n+1)]

    for road in roads:
        graph[road[0]].append(road[1])
        graph[road[1]].append(road[0])

    queue = deque()
    queue.append(destination)
    dist = [-1 for _ in range(n+1)]
    dist[destination] = 0
    while (queue):
        start = queue.popleft()
        for adj in graph[start]:
            if dist[adj] == -1:
                queue.append(adj)
                dist[adj] = dist[start]+1

    return [dist[i] for i in sources]
