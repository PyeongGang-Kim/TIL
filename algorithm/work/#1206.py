import sys
sys.stdin = open("#1206_input.txt")

T = 10
for t in range(1, T+1):
    result = 0
    N = int(input())
    nl = list(map(int, input().split()))
    i = 2
    while i < N-2:
        max = nl[i + 2]
        for j in range(-2, 2):
            if j != 0:
                if nl[i + j] > max:
                    max = nl[i + j]
        if max <= nl[i]:
            result += nl[i]-max
            i += 2
        i += 1

    print('#{} {}'.format(t, result))