import sys
'''
뒤에서부터 채워나가는 dp
오늘 골랐을 때와 다음날의 최대값 중 최대값을 고르면 된다.

3 10    5 20    1 10    1 20    2 15    4 40    2 200   퇴사
                                                        0

3 10    5 20    1 10    1 20    2 15    4 40    2 200   퇴사
                                                0       0

3 10    5 20    1 10    1 20    2 15    4 40    2 200   퇴사
                                        0       0        0

3 10    5 20    1 10    1 20    2 15    4 40    2 200   퇴사
                                15      0       0       0

3 10    5 20    1 10    1 20    2 15    4 40    2 200   퇴사
                         35     15      0       0       0

3 10    5 20    1 10    1 20    2 15    4 40    2 200   퇴사
                 45      35     15      0       0       0

3 10    5 20    1 10    1 20    2 15    4 40    2 200   퇴사
         45      45      35     15      0       0       0

3 10    5 20    1 10    1 20    2 15    4 40    2 200   퇴사
 45      45      45      35     15      0       0       0
 
 
 
%%%%
오늘 못 골랐을 때에는 무조건 다음날의 최대값을 골라줘야 함.
 '''

N = int(sys.stdin.readline())
nl = []
for _ in range(N):
    nl.append(list(map(int, sys.stdin.readline().split())))
D = [0]*(N+1)
r = 0
for i in range(N-1, -1, -1):
    if nl[i][0] + i <= N:
        D[i] = max(D[i+nl[i][0]] + nl[i][1], D[i+1])
    else:
        D[i] = D[i+1]
print(D[0])