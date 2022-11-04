# https://school.programmers.co.kr/learn/courses/30/lessons/43105

# dp 기본 문제
'''
위에서 아래로 내려오면 양 끝쪽은 아래에 1개 밖에 없음.
=> 조건문 또 추가해주어야함
=> 생각을 바꿔서 밑에서 두번째 줄부터 시작해서 아래 두개 중 큰 것 이용
=> 조건문 필요 X
'''


def solution(triangle):
    answer = 0

    for x in range(len(triangle)-2, -1, -1):
        for y in range(len(triangle[x])):
            triangle[x][y] += max(triangle[x+1][y], triangle[x+1][y+1])

    answer = triangle[0][0]
    return answer
