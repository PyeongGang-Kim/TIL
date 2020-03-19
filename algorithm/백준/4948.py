import sys
input = sys.stdin.readline
pl = [1] * 246913
pl[1] = 0
pl[0] = 0
i = 2
while i < 498:
    tmp = i ** 2
    while tmp < 246913:
        pl[tmp] = 0
        tmp += i
    i += 1
i = 3
su = 1
while i < 246913:
    t = i
    s = 0
    while t:
        s += pl[t]
        t &= t - 1
    su += pl[i]
    pl[i] += su - s
    i += 1

r = []
a = int(input())
while a:
    b = 2 * a
    su = 0
    while b:
        su += pl[b]
        b &= b - 1
    while a:
        su -= pl[a]
        a &= a - 1

    r.append(str(su))
    a = int(input())
print('\n'.join(r))