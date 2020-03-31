i = 1
N = 100
while i < N:
    print(i&(i-1), i - (i&(-i)))
    i += 1