import sys
'''
1원짜리 2원짜리 동전이 있을 때 10 원을 주는 방법을 살펴보면
1 원짜리 10개
1 원짜리 8개 2원짜리 1개
1 원짜리 6개 2원짜리 2개
...
2 원짜리 5개
이런 방법들이 존재한다.
동전을 주는 순서는 상관이 없으므로
1원짜리로 전부 주는 방법과
2원짜리를 1번, 2번, 3번 주는 방법 등을 확인하면 된다.
각각의 금액을 만드는 방법을 위에서 내려온 결과(현재 동전을 사용하지 않음)
+ 현재 행에서 동전을 추가할 수 있는 경우(현재 동전을 사용하는 경우)
두 방법에 대해서 가능하다.

%%
동전의 가치가 내가 구하고자 하는 값 보다 클 경우도 고려해줘야 한다.

%%%
이차원 배열을 만들지 않고 코인들에 대해서 실시하면 된다.
10원을
2원 3원으로 만드는 경우
    0   1   2   3   4   5   6   7   8   9   10
0원 1   0   0   0   0   0   0   0   0   0   0       
2원 1   0   1   0   1   0   1   0   1   0   1           
3원 1   0   1   1   1   1   2   1   1   2   2
이런식인데
        
0원일 때 1   0   0   0   0   0   0   0   0   0   0 인데
2원일 때 1   0   0   0   0   0   0   0   0   0   0 이전의 행에서
현재 코인을 사용할 수 있는 경우에 대해서 추가적으로 더해주기만 하면된다.
-> 2차원 배열이 아니라 그냥 이전에 사용했던 행 하나를 다시 사용하면 연산을 줄이고
메모리 사용도 줄일 수 있다.
'''
T = int(sys.stdin.readline())
r = []
for tc in range(T):
    N = int(sys.stdin.readline())
    nl = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    D = [0 for _ in range(M+1)]
    D[0] = 1
    for c in nl:
        for i in range(c, M+1):
            D[i] += D[i-c]
    r.append(str(D[M]))
print('\n'.join(r))


# import sys; input = lambda: sys.stdin.readline().rstrip()
#
# def solve(coins, m) :
#     v = [1] + [0 for i in range(m)]
#     for c in coins :
#         for i in range(c, len(v)) :
#             v[i] += v[i-c]
#     return v[m]
#
# tc = int(input())
# for t in range(tc) :
#     n = int(input())
#     c = list(map(int, input().split()))
#     m = int(input())
#     print(solve(c, m))