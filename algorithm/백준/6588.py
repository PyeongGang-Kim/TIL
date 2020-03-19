pl = [i & 1 for i in range(1000001)]
pl[1] = 0
i = 3
while i < 1001:
    j = i ** 2
    t = i * 2
    while j < 1000001:
        pl[j] = 0
        j += t
    i += 2
r = []
n = int(input())
while n:
    a = 3
    b = n - 3
    while (not pl[a] or not pl[b]) and a <= b:
        a += 2
        b = n - a
    r.append('{} = {} + {}'.format(n, a, b) if a <= b else "Goldbach's conjecture is wrong.")

    n = int(input())
print('\n'.join(r))