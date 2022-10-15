import sys
input = sys.stdin.readline

myinput = input()
alpha_list = []
value = 0

for w in myinput:
    if w.isalpha():
        alpha_list.append(w)
    else:
        value += int(w)

alpha_list.sort()
if value > 0:
    alpha_list.append(str(value))

print(''.join(alpha_list))
