# T
# 노드의 개수 N과 리프 노드의 개수 M, 값을 출력할 노드 번호 L
# 노드 인덱스, 값

T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    nl = [0] * (N+1)
    for m in range(M):
        i, v = map(int, input().split())
        nl[i] = v
    print(nl)

