import sys
input = sys.stdin.readline


def bin(s, e):
    if s == e:
        if a[s] > -a[i]:
            return s
        else:
            return s+1
    m = (s + e)>>1
    if a[m] > -a[i]:
        return bin(s, m)
    else:
        return bin(m+1, e)


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(n):
    a[i] -= b[i]
cnt = 0
a.sort()
idx1 = 0
idx2 = 1
for i in range(n-1):
    cnt += n - bin(i+1, n-1)
print(cnt)
