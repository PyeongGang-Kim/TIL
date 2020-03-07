n = int(input())
a = input()
cnt = 0
for i in range(n):
    if a[i] == '(':
        cnt += 1
r = 0
if cnt == (n>>1):
    cnt = 0
    i = 0
    while i < n:
        if a[i] == ')':
            cnt -= 1
        else:
            cnt += 1
        if cnt < 0:
            for j in range(i+1, n):
                if a[j] == ')':
                    cnt -= 1
                else:
                    cnt += 1
                if not cnt:
                    r += j - i + 1
                    i = j
                    break
        i += 1
    if cnt:
        print(-1)
    else:
        print(r)
else:
    print(-1)
