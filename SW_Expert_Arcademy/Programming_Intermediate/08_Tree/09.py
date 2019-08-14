def sumh(num):
    if num > N:
        return 0
    if nl[num]:
        return nl[num]
    else:
        return sumh(num*2) + sumh(num*2 + 1)


T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    nl = [0] * (N+1)
    for m in range(M):
        i, v = map(int, input().split())
        nl[i] = v
    print("#{} {}".format(t, sumh(L)))