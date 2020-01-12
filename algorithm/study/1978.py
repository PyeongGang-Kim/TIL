import sys

input = sys.stdin.readline
N = int(input())
nl = [i & 1 for i in range(1001)]
nl[1] = False
nl[2] = True
num = 3
while num < 33:
    if nl[num]:
        tmp = num * num
        while tmp < 1000:
            nl[tmp] = False
            tmp += num
    num += 2

cnt = 0
for num in map(int, input().split()):
    if nl[num]:
        cnt += 1

print(cnt)