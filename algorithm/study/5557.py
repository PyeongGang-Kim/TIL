import sys
'''
각 행이 이전 행에 의해서 채워지는 구조다
첫번째 값에 대해선 이전 행이 없으므로 직접 입력해 준다.
두번째 값부터는 이전 행이 있으므로 이전 행을 참고하여 데이터를 작성한다.
두번째 값(3)은 이전행의 값 8 에 3을 더하거나 뺀 값(5, 11)이다.
5와 11의 위치에는 이전행의 값(8)이 나올 수 있는 갯수만큼 생기게 된다(더해준다)
끝까지 반복한다.
맨 맨 마지막 행에서 우리가 찾는 값이 있는 인덱스는 인풋 값 중 맨 마지막 값과 같다.

     0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20
     
8    0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0
3    0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0
2    0,  0,  0,  1,  0,  0,  0,  1,  0,  1,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0
4    0,  0,  0,  1,  0,  1,  0,  1,  0,  1,  0,  1,  0,  1,  0,  0,  0,  1,  0,  0,  0
8    0,  1,  0,  1,  0,  1,  0,  0,  0,  1,  0,  1,  0,  1,  0,  1,  0,  1,  0,  1,  0
7    0,  0,  1,  0,  1,  0,  1,  0,  2,  0,  2,  0,  2,  0,  0,  0,  1,  0,  1,  0,  1
2    1,  0,  1,  0,  2,  0,  3,  0,  3,  0,  4,  0,  2,  0,  3,  0,  1,  0,  2,  0,  1
4    2,  0,  3,  0,  4,  0,  5,  0,  4,  0,  6,  0,  4,  0,  6,  0,  3,  0,  3,  0,  1
0    4,  0,  6,  0,  8,  0, 10,  0,  8,  0, 12,  0,  8,  0, 12,  0,  6,  0,  6,  0,  2
8    8,  0, 12,  0,  8,  0, 12,  0, 10,  0, 12,  0, 10,  0, 10,  0,  8,  0, 12,  0,  8
8


'''

N = int(sys.stdin.readline())
N2 = N-1
r = 0
nl = list(map(int, sys.stdin.readline().split()))
ra = range(21)
dl = [[0 for _ in ra] for _ in range(N2)]
dl[0][nl[0]] = 1
for j in range(1, N2):
    for i in ra:
        tmp = dl[j-1][i]
        if tmp:
            tmp1, tmp2 = i + nl[j], i - nl[j]
            if tmp1 < 21:
                dl[j][tmp1] += tmp
            if tmp2 >= 0:
                dl[j][tmp2] += tmp
print(dl[-1][nl[-1]])
