import sys
sys.stdin = open('test2_input.txt')


def mkr(d = 0):
    global result
    tmp = 0
    tmpx, tmpy = nl[0], nl[1]
    for i in arr:
        tmp += abs(tmpx - nl[i * 2 + 4]) + abs(tmpy - nl[i * 2 + 5])
        tmpx, tmpy = nl[i * 2 + 4], nl[i * 2 + 5]
    tmp += abs(tmpx - nl[2]) + abs(tmpy - nl[3])
    if tmp > result:
        return
    if d == N:
        if tmp < result:
            result = tmp
        return
    for i in range(N):
        if i not in arr:
            arr.append(i)
            mkr(d+1)
            arr.pop()


T = int(input())
for t in range(1, T+1):
    N = int(input())
    nl = list(map(int, input().split()))
    company = nl[0:2]
    home = nl[2:4]
    arr = []
    tmp = 0
    tmpx, tmpy = nl[0], nl[1]
    for i in range(N):
        tmp += abs(tmpx - nl[i * 2 + 4]) + abs(tmpy - nl[i * 2 + 5])
        tmpx, tmpy = nl[i * 2 + 4], nl[i * 2 + 5]
    tmp += abs(tmpx - nl[2]) + abs(tmpy - nl[3])
    result = tmp
    mkr()
    print('#{} {}'.format(t, result))
    # print(fr)
    # print(result)
