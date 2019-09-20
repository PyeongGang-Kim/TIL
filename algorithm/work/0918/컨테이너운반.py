import sys
sys.stdin = open('컨테이너운반.txt')


T = int(input())
for t in range(1, T+1):
        N, M = map(int, input().split())
        nl = sorted(list(map(int, input().split())), reverse=True)
        ml = sorted(list(map(int, input().split())), reverse=True)
        cl = [0]*N
        r = 0
        for i in range(M):
            for j in range(N):
                if nl[j] <= ml[i] and not cl[j]:
                    cl[j] = 1
                    r += nl[j]
                    break
                    break
        print('#{} {}'.format(t, r))