D = [0,1,3]

for t in range(1, int(input())+1):
    N = int(input())
    if N >= len(D):
        k = N-len(D) + 1
        while k:
            k -= 1
            D.append(D[-1]+(D[-2]<<1))
    print('#{} {}'.format(t, D[N]))