while True:
    try:
        a, b = map(int, input().split())

        cnt = 0
        for i in range(a, b + 1):
            tmp = str(i)
            tmp2 = set()
            for t in tmp:
                tmp2.add(t)
            if len(tmp) == len(tmp2):
                cnt += 1
        print(cnt)
    except:
        break
