T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    K = int(input())
    N = int(input())
    M = int(input())
    lst = list(map(int, input().split()))
    minus = 0
    count = 0

    for x in range(0, M):
        minus += lst[x + 1] - lst[x]
        if minus > K:
            minus = lst[x + 1] - lst[x]
            if minus > K:
                break
            else:
                count += 1
        else:
            count += 1
    print('#' + str(test_case), count)