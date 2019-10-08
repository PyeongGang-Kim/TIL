T = int(input())
for t in range(1, T+1):
    S = input()
    st = []
    r = 0
    d = {'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0}
    try:
        for s in S:
            if s == 'c':
                st.append(1)
                d[s] += 1
            elif s == 'k':
                if d[s] < d['a']:
                    r = max(len(st), r)
                    st.pop()
                    d[s] += 1
                else:
                    r = -1
                    break
            elif s == 'r':
                if d[s] < d['c']:
                    d[s] += 1
                else:
                    r = -1
                    break
            elif s == 'a':
                if d[s] < d['o']:
                    d[s] += 1
                else:
                    r = -1
                    break
            else:
                if d[s] < d['r']:
                    d[s] += 1
                else:
                    r = -1
                    break
    except:
        r = -1
    if len(st):
        r = -1
    else:
        tmp = d['c']
        for i in d.values():
            if i != tmp:
                r = -1
                break
    print('#{} {}'.format(t, r))