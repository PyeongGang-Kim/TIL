import sys
sys.stdin = open('이진탐색_input.txt')

def win(l, r, f, cnt= 0):
    c =  (l + r)//2
    if c>f:
        cnt += 1
        return win(l, c, f, cnt)
    elif c<f:
        cnt += 1
        return win(c, r, f, cnt)
    else:
        return cnt


T = int(input())
for t in range(1, T+1):
    l, a, b = map(int, input().split())
    A = win(1, l, a)
    B = win(1, l, b)
    if A<B:
        print('#{} A'.format(t))
    elif A>B:
        print('#{} B'.format(t))
    else:
        print('#{} 0'.format(t))