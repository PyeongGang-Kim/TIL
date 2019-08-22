import sys
sys.stdin = open('종이붙이기.txt')


def llll(p=0):
    if p == N:
        return 1
    if p > N:
        return 0
    return llll(p+1) + 2 * llll(p+2)


def llll2(p):
    if len(nl)>p:
        return nl[p]
    else:
        nl.append(llll2(p-1) + 2 * llll2(p-2))
        return nl[p]


def llll3(N):
    tmp=0
    for i in range(int(N/2)+1):
        tmp+=int(round(combi(N-i,i)*2**i))
    return tmp


def llll4(N):
    if len(nl2) > N:
        if nl2[N]:
            return nl2[N]
    else:
        while len(nl2)<=N:
            nl2.append(0)
        tmp=0
        for i in range(int(N/2)+1):
            tmp+=int(round(combi(N-i,i)*2**i))
        nl2[N] = tmp
        return nl2[N]


def combi(n, k):
    result = 1
    k = min(n-k, k)
    for i in range(1, k+1):
        result*=(n+1-i)/i
    return result


T = int(input())
nl = [1, 1]
nl2 = [1, 1]
for t in range(1, T+1):
    N = int(input())//10
    # print('#{}'.format(t), llll())
    # print(llll2(N))
    # print(llll3(N))
    print('#{}'.format(t), llll4(N))