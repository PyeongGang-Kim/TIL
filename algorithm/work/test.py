for t in range(1, int(input())+1):
    N = int(input())
    S = input()
    r = 0
    for i in range(2, len(S)+1):
        chk = 0
        for j in range(0, len(S)+1-i):
            tmp = S[j:j+i]
            for k in range(j+1, len(S)+1-i):
                if tmp  == S[k:k+i]:
                    chk = 1
                    break
            if chk:
                break
        if chk:
            r = i
            continue
        else:
            break
    print('#{} {}'.format(t, r))