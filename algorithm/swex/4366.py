T = int(input())
for t in range(1, T+1):
    bn = list(input())
    tn = list(input())
    bns = set()
    tns = set()
    for i in range(len(bn)):
        if bn[i] == '1':
            bn[i] = '0'
            tmp = 0
            for j in range(len(bn)):
                tmp *= 2
                tmp += int(bn[j])
            bns.add(tmp)

            bn[i] = '1'
        else:
            bn[i] = '1'
            tmp = 0
            for j in range(len(bn)):
                tmp *= 2
                tmp += int(bn[j])
            bns.add(tmp)

            bn[i] = '0'
    for i in range(len(tn)):
        if tn[i] == '0':
            bn[i] = '1'
            tmp = 0
            for j in range(len(tn)):
                tmp *= 2
                tmp += int(tn[j])
            tns.add(tmp)

            bn[i] = '0'
            bn[i] = '2'
            tmp = 0
            for j in range(len(tn)):
                tmp *= 2
                tmp += int(tn[j])
            tns.add(tmp)

            bn[i] = '0'
        elif tn[i] == '1':
            bn[i] = '0'
            tmp = 0
            for j in range(len(tn)):
                tmp *= 2
                tmp += int(tn[j])
            tns.add(tmp)

            bn[i] = '1'
            bn[i] = '3'
            tmp = 0
            for j in range(len(tn)):
                tmp *= 2
                tmp += int(tn[j])
            tns.add(tmp)

            bn[i] = '1'
        else:
            bn[i] = '0'
            tmp = 0
            for j in range(len(tn)):
                tmp *= 2
                tmp += int(tn[j])
            tns.add(tmp)

            bn[i] = '2'
            bn[i] = '1'
            tmp = 0
            for j in range(len(tn)):
                tmp *= 2
                tmp += int(tn[j])
            tns.add(tmp)

            bn[i] = '2'
    print(bns.intersection(tns))