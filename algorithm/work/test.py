import sys
sys.stdin = open('asdf.txt')


T = int(input())
for t in range(1, T+1):
    A, B, C = map(int, input().split())
    if A > B:
        A = B
    print('#{} {}'.format(t, C//A))