'''
시간초과

'''

T = int(input())
for t in range(1, T+1):
    X, Y, Z, A, B, C, N = map(int, input().split())
    if N == 1:
        print('#{} {}'.format(t, X*Y*Z))
    else:
        nl = [0 for i in range(N)]
        for z in range(Z):
            for y in range(Y):
                t1, t2 = divmod(X, N)
                sc = (A + abs(B-y) + abs(C-z)) % N
                for i in range(t2):
                    nl[sc] += 1
                    sc = (sc + 1) % N
                for i in range(N):
                    nl[i] += t1

        r = ['#%d' % t]
        for n in nl:
            r.append(str(n))
        print(' '.join(r))