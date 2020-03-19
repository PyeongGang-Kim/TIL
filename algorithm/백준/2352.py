'''
최장 증가 수열 문제

차례대로 골라서 순서가 역이 아닌(곂치는)것들을 최대한 골라야 한다.
최장 증가 수열 문제가 된다.
'''
def bs(s, e, n):
    m = (s+e)//2
    if D[m] < n:
        if D[m+1] < n:
            bs(m, e, n)
            return
        else:
            D[m+1] = n
            return
    else:
        if D[m-1] < n:
            D[m] = n
        else:
            bs(s, m , n)
            return

N = int(input())
nl = list(map(int, input().split()))
D = [0]
for n in nl:
    if n > D[-1]:
        D.append(n)
    elif n > D[-2]:
        D[-1] = n
    else:
        bs(0, len(D)-1, n)
print(len(D)-1)