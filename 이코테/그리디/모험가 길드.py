# 문제를 잘못 이해했다 !
# 무조건 넣는게 아니라 안 들어갈수도. 그룹 수만 최대로

'''
import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

nums.sort(reverse=True)

start = 0
count = 0

while (start < N):
    start += nums[start]
    count += 1

if start == N-1:
    count += 1

print(count)
'''

from re import L
import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
nums.sort()

start = 0
count = 0
final = 0

for num in nums:
    count += 1
    if (count >= num):
        final += 1
        count = 0

print(final)
