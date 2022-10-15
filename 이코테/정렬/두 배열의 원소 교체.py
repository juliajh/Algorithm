
n, k = map(int, input().split())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_list.sort()
b_list.sort(reverse=False)

for i in range(k):
    a_list[i] = b_list[len(b_list)-1-i]
    b_list[i] = a_list[len(a_list)-1-i]

print(sum(a_list))
