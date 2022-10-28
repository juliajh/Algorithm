# Level 2
# 채감 난이도: 2/5
# 순열이 바로 생각나서 비교적 쉽게 푼 문제

import itertools


def solution(k, dungeons):
    new_list = []
    answer = 0

    for i in range(1, len(dungeons)+1):
        new_list += list(itertools.permutations(dungeons, i))
    for mylist in new_list:
        count = 0
        now = k
        for mm in mylist:
            if (now <= 0):
                continue
            if (mm[0] > now):
                continue
            now -= mm[1]
            count += 1
        if (answer < count):
            answer = count
    return answer
