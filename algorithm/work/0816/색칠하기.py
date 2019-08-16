import sys
sys.stdin = open('색칠하기_input.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    nl = [[[0,0] for _ in range(10)] for _ in range(10)]
    for n in range(N):
        x1, y1, x2, y2, c = map(int, input().split())
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                nl[y][x][c-1]=c
    cnt = 0
    for j in range(10):
        for i in range(10):
            if nl[j][i][0] and nl[j][i][1]:
                cnt += 1

    print('#{} {}'.format(t, cnt))