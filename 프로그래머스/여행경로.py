from collections import defaultdict

tickets = [["ICN", "AAA"], ["ICN", "AAA"], [
    "BBB", "ICN"]]


def solution(tickets):
    answer = ['ICN']
    places = []
    '''
    for i in range(len(tickets)):
        for j in range(2):
            if tickets[i][j] not in places and tickets[i][j] != 'ICN':
                places.append(tickets[i][j])

    places.sort(reverse=True)
    places.append('ICN')
    places.reverse()

    graph = [[False for i in range(len(places))] for j in range(len(places))]

    for i in range(len(tickets)):
        start = places.index(tickets[i][0])
        end = places.index(tickets[i][1])
        graph[start][end] = True
    '''

    def init_graph():
        routes = defaultdict(list)
        for key, value in tickets:
            routes[key].append(value)
        print(routes)
        return routes

    # 재귀 호출을 사용한 DFS
    def dfs(key):
        if len(answer) == N + 1:
            return answer

        for idx, country in enumerate(routes[key]):
            routes[key].pop(idx)

            # answer  # deepcopy
            answer.append(country)

            ret = dfs(country)
            print(ret)
            if ret:
                return ret  # 모든 티켓을 사용해 통과한 경우

            routes[key].insert(idx, country)  # 통과 못했으면 티켓 반환
            answer.pop()

    routes = init_graph()
    for r in routes:
        routes[r].sort()

    N = len(tickets)
    answer = dfs("ICN")

    return answer


print(solution(tickets))
