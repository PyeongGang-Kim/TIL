'''
현재 수는 내 전에 사람이 나를 이기지 못하게 하기 위한 최선의 수
내 이전의 수는 좀전에 구한 최선의 수를 고르지 못하게 하기 위한 최대의 수
=> 내 이전의 수가 현재의 수 N 에 대해서
N = (N//2+1)//2-1
이 된다.

N을 25까지 미리 구해본 결과표
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
  b a a a a b b b b a  a  a  a  a  a  a  a  a  a  a  a  a  a  a  a

'''


T = int(input())
for t in range(1, T+1):
    N = int(input())
    while N > 25:
        N = (N//2+1)//2-1
    if N == 1 or (6 <= N <= 9):
        print('#%d Bob' %t)
    else:
        print('#%d Alice' %t)
