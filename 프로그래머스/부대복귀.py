# road 순서대로 bfs할 경우 시간 초과
# 그래서 거꾸로 destination 부터 !

from collections import deque


def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n+1)]

    # 인접 리스트
    for road in roads:
        graph[road[0]].append(road[1])
        graph[road[1]].append(road[0])
    # 처음에는 인접 행렬로 하다가 그럴 필요 없을 것 같아서 수정함.

    queue = deque()
    queue.append(destination)

    # destination ~ 각 인덱스 별로 최단 거리 겸 visited 여부 표현
    dist = [-1 for _ in range(n+1)]
    dist[destination] = 0
    while (queue):
        start = queue.popleft()
        for adj in graph[start]:
            if dist[adj] == -1:  # 아직 방문 안했다면
                queue.append(adj)
                # 출발한 위치의 dist에 +1 저장. 기존의 최단 거리에 더해주는 개념.
                dist[adj] = dist[start]+1

    return [dist[i] for i in sources]
