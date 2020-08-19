M = int(input())
s = input()
N = len(s)//M
r = []
for m in range(M):
    for n in range(N):
        if n & 1:
            r.append(s[(n+1)*M-1-m])
        else:
            r.append(s[m+n*M])

print(''.join(r))