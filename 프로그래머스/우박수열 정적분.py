# https://school.programmers.co.kr/learn/courses/30/lessons/134239

def solution(k, ranges):
    answer = []
    y_list = [k]
    area_list = []
    while (k > 1):
        if (k % 2 == 0):
            k = k//2
            y_list.append(k)
        else:
            k = k*3+1
            y_list.append(k)

    for i in range(len(y_list)-1):
        area_list.append((y_list[i]+y_list[i+1])/2)
    print(area_list)

    def getArea(start, end):
        end = len(y_list)-1+end
        num = 0
        if start > end:
            return -1.0
        for i in range(start, end, 1):
            num += area_list[i]
        return num

    for r in ranges:
        answer.append(getArea(r[0], r[1]))

    return answer
