# https://school.programmers.co.kr/learn/courses/30/lessons/118667
# Level 2
# 시간 초과가 나서 어떻게 줄일까 고민 계속 했는데
# 답이 너무 허무해 ㅠ
# limit 추가해서 while문 계속 도는 것 제한
# sum 함수보다는 total 변수써서 직접 계산

from collections import deque
import queue


def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    tot1 = sum(queue1)
    tot2 = sum(queue2)
    limit = len(queue1)*4

    while (queue1 and queue2) and limit != answer:
        if (tot1 == tot2):
            return answer
        elif (tot1 > tot2):
            num = queue1.popleft()
            queue2.append(num)
            answer += 1
            tot1 -= num
            tot2 += num
        elif (tot2 > tot1):
            num = queue2.popleft()
            queue1.append(num)
            answer += 1
            tot2 -= num
            tot1 += num
    return -1
