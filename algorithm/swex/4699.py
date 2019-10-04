'''

m[i][j] 에는 주어진 인풋(S)의 i에서 시작해서 j까지 이루어진 펠린드롭만든 최소값이다.
1글자인 경우 문자열을 펠린드롭으로 만들기 위한 비용은 0원이므로 각각 초기화 시켜 준다.
1글자부터 len(S)글자까지 키워가면서 확인한다.
    각 글자수일때 모든 경우의 수에 대하여 비용을 계산한다.
    (2글자일 경우  0-1, 1-2, 2-3 등등)
    최소 비용은 지금보다 한글자 작을때에 삭제하거나 삽입 혹은 유지해서 만들어진다.
    왼쪽을 삽입 혹은 삭제한 값과 오른쪽을 삽입 혹은 삭제한 값
    만약 양 끝이 같으면 삭제 혹은 삽입을 할 필요가 없다.

따라서 삽입 혹은 삭제할 때의 비용이 작은것을 선택하면 된다.

'''

m = [[0 for _ in range(2002)] for _ in range(2002)]

T = int(input())
for t in range(1, T+1):
    L, K = map(int, input().split())
    S = input()
    price = dict()
    for k in range(K):
        t1, t2 = map(int, input().split())
        price[chr(97+k)] = min(t1, t2)

    for i in range(L):
        m[i][i] = 0
        for j in range(i+1, L):
            m[i][j] = 0xffffffff

    for k in range(1, L):
        i = 0
        j = k
        for _ in range(L-k):
            m[i][j] = min(m[i][j], m[i+1][j]+price[S[i]], m[i][j-1]+price[S[j]])
            if S[i] == S[j]:
                m[i][j] = min(m[i][j], m[i+1][j-1])
            i += 1
            j += 1
    print('#{} {}'.format(t, m[0][L-1]))


