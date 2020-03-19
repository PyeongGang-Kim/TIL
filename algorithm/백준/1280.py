import sys
input = sys.stdin.readline
n = int(input())
m = 10 ** 9 + 7
c = [0] * 200001
d = [0] * 200001
r = 1
i = 1
x = int(input()) + 1
t = x
while t <= 200000:
    c[t] += 1
    d[t] += x
    t += t & -t
s = x
while i < n:
    x = int(input()) + 1
    if i:
        t = x
        p = q = 0
        while t:
            p += c[t]
            q += d[t]
            t &= t - 1
        r = r * (p * x - q + s - q - (i - p) * x) % m
    t = x
    while t <= 200000:
        c[t] += 1
        d[t] += x
        t += t & -t
    s += x
    i += 1
print(r)