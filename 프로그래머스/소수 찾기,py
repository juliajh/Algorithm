# https://school.programmers.co.kr/learn/courses/30/lessons/42839

# 방법은 빨리 찾았으나 튜플 문법을 잘 몰라서 헤맸음.
# int(''.join(i))  튜플 i 원소 이어주기

from itertools import permutations


def solution(numbers):
    answer = 0

    # 소수인지 찾기
    def is_prime_num(n):
        if n < 2:
            return False

        for i in range(2, n//2+1):
            if n % i == 0:
                return False

        return True

    nums = []
    ss = []
    result = []
    for num in numbers:
        nums.append(num)

    for i in range(1, len(numbers)+1):   # list extend => list의 기본 원소처럼 추가
        ss.extend(permutations(numbers, i))

    for i in ss:                        # 튜플 내 원소들 이어주기. 튜플 문법 공부 더 하기!
        result.append(int(''.join(i)))  # int로 변환하여 011=11와 같도록.

    for r in set(result):
        if is_prime_num(r):
            answer += 1

    return answer
