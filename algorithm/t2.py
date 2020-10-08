# 모든 비트 짝수개인지 확인한다.
# 모든 비트 조합을 구한다.


# 모든 합 조합을 구한다.
# 작은 합 조합부터


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nl = list(map(int, input().split()))
    tmp2 = set()
    tmp = set()
    tmpp2 = set([0])
    # print(tmp)
    for i in range(N):
        tmpp = set([0])
        for num in tmpp2:
            if num^nl[i] not in tmp:
                tmpp.add(num^nl[i])

            else:
                if not num^nl[i]:
                    tmp2.add(num)
                    tmp2.add(nl[i])
        tmp = tmp.union(tmpp)
        tmpp2 = tmpp
    tmp = sorted(list(tmp))
    print(tmp)
    print(tmp2)
    for i in range(1, len(tmp)-1):
        for j in range(i+1, len(tmp)):
            if not tmp[i]^tmp[j]:
                print(1111111)
                break