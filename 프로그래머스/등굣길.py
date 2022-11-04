# https://school.programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    answer = 0
    graph = [[0]*(m+1) for _ in range(n+1)]  # graph의 크기를 (m+1)*(n+1)로 하여

    graph[1][1] = 1  # 맨 윗줄과 맨 왼쪽 줄에 1을 대입하는 과정을 줄여줌
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles:  # 좌표 거꾸로 주의
                graph[i][j] = 0  # 0으로 저장할 경우 합해도 그대로
                continue
            graph[i][j] = (graph[i-1][j]+graph[i][j-1])

    answer = graph[-1][-1] % 1000000007
    return answer


'''
def solution(m, n, puddles):
    answer = 0
    graph = [[0 for _ in range(m)] for _ in range(n)]  

    for i in range(m):             graph의 크기를 m*n로 할 경우 따로 1을 해주어야함.
        graph[0][i] = 1            

    for j in range(n):
        graph[j][0] = 1

    for puddle in puddles:
        graph[puddle[1]-1][puddle[0]-1] = -1

    for i in range(1, m):                어디서 꼬인듯 ..?
        for j in range(1, n):
            if graph[j][i] == -1:
                graph[j][i] = 0
                continue
            graph[j][i] = (graph[j][i-1]+graph[j-1][i])

    answer = graph[-1][-1] % 1000000007

    return answer
'''
