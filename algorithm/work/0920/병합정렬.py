import sys
sys.stdin = open('병합정렬.txt')


def mergesort(left, right):
    global cnt
    if len(left) > 1:
        left = mergesort(left[:len(left)//2], left[len(left)//2:])
    if len(right) > 1:
        right = mergesort(right[:len(right)//2], right[len(right)//2:])
    fl, rl, fr, rr = 0, len(left), 0, len(right)
    if left[-1] > right[-1]:
        cnt += 1
    tmp = []
    while fl != rl or fr != rr:
        if fl == rl:
            if fr == rr:
                break
            tmp.append(right[fr])
            fr += 1
        elif fr == rr:
            tmp.append(left[fl])
            fl += 1
        else:
            if right[fr] > left[fl]:
                tmp.append(left[fl])
                fl += 1
            else:
                tmp.append(right[fr])
                fr += 1
    return tmp


T = int(input())
for t in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    a = mergesort(a[:N//2], a[N//2:])
    print('#{} {} {}'.format(t, a[N//2], cnt))