import sys
sys.stdin = open('이진수2.txt')

T = int(input())
for t in range(1, T+1):
    N = float(input())
    r = ['#%d ' %t]
    for i in range(1, 13):
        k=2**(-i)
        if N >= k:
            r.append('1')
            N -= k
            if N == 0:
                break
        else:
            r.append('0')
    if N:
        print('#%d overflow' %t)
    else:
        print(''.join(r))