from collections import deque
import queue


def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque([0 for _ in range(bridge_length)])
    bridgeWeight = 0   # queue의 합을 담은 변수
    while queue:
        a = queue.popleft()
        bridgeWeight -= a
        if truck_weights:
            # sum(queue)로 계산하면 시간 초과
            if bridgeWeight + truck_weights[0] <= weight:
                t = truck_weights.pop(0)
                queue.append(t)
                bridgeWeight += t
            else:
                queue.append(0)
        answer += 1
    return answer
