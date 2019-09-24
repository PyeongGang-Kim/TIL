T = int(input())
for t in range(1, T+1):
    a, b = input().split()
    cnt = 0
    i = 0
    if len(b) != 1:
        while i < len(a) - len(b) + 1:
            chk = 0
            for j in range(len(b)):
                if a[i+j] != b[j]:
                    chk = 1
                    break
            if not chk:
                cnt += 1
                i += len(b) - 1
            i += 1
        print('#{} {}'.format(t, len(a) - (len(b) - 1) * cnt))
    else:
        print('#{} {}'.format(t, len(a)))