import sys
input = sys.stdin.readline


'''
m은 남은 쿼리 갯수
쿼리 갯수만큼 미리 땡겨놓은 리스트를 기준으로 세그먼트 구간합 구하기
인덱스를 저장할 배열 하나
인덱스 저장한 배열에서 꺼내와서 그거 오른쪽 구간합 구하기
현재 인덱스를 0으로 바꾸고 갱신
현재 dvd를 m번째 위치로 변경

'''
T = int(input())
while T:
    T -= 1
    r = []
    n, m = map(int, input().split())
    N = n + m
    nl = [0] * (N + 1)
    nl[m+1] = 1
    tmp = m + 2
    i = 2
    idxl = [i for i in range(m, N+1)]
    while tmp <= N:
        tmp2 = tmp
        s = 0
        while tmp2:
            s += nl[tmp2]
            tmp2 &= (tmp2 - 1)

        nl[tmp] = i - s
        i += 1
        tmp += 1


    for number in map(int, input().split()):
        tmp = idxl[number] - 1
        s = 0
        while tmp:
            s += nl[tmp]
            tmp &= tmp - 1
        tmp = idxl[number]
        while tmp <= N:
            nl[tmp] -= 1
            tmp += tmp & -tmp
        r.append(str(s))
        tmp = m
        idxl[number] = m
        while tmp <= N:
            nl[tmp] += 1
            tmp += tmp & -tmp
        m -= 1
    print(' '.join(r))

