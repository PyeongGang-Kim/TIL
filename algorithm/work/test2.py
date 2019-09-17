import sys
sys.stdin = open('asdf1.txt')


def cal(numstr):
    i = 0
    r = len(numstr) - 1
    ns = 0
    while i != r:
        tmp = int(numstr[i])
        ns += 45*(r-i)*(10**(r-i-1))*tmp
        for j in range(1, tmp):
            ns += j * 10**(r-i)
        ns += tmp*(int(numstr[i+1:])+1)
        i += 1
    for k in range(1, int(numstr[-1])+1):
        ns += k
    return ns


T = int(input())
for t in range(1, T+1):
    a, b = input().split()
    if a != '0':
        a = str(int(a) - 1)
    print('#{} {}'.format(t, cal(b)-cal(a)))