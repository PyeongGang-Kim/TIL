import sys
sys.stdin = open('특별한정렬_input.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    nl = list(map(int, input().split()))
    print('#{}'.format(t), end=' ')

    for i in range(N-1):
        for j in range(N-1-i):
            if nl[j] < nl[j + 1]:
                nl[j], nl[j + 1] = nl[j+1], nl[j]


    for n in range(10):
        if nl:
            if n%2:
                tmp = nl.pop()
            else:
                tmp = nl.pop(0)
            print(tmp, end=' ')
        else:
            break
    print()