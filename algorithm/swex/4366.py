'''
각 자리 숫자들을 하나씩 바꿔서 10진수로 바꾼 값을 셋에 넣어준다.
2진수를 변환해서 저장한 셋과 3진수를 변환해서 저장한 셋의 교집합을 구한다.
'''

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
            tn[i] = '1'
            tmp = 0
            for j in range(len(tn)):
                tmp *= 3
                tmp += int(tn[j])
            tns.add(tmp)
            tn[i] = '2'
            tmp = 0
            for j in range(len(tn)):
                tmp *= 3
                tmp += int(tn[j])
            tns.add(tmp)

            tn[i] = '0'
        elif tn[i] == '1':
            bn[i] = '0'
            tmp = 0
            for j in range(len(tn)):
                tmp *= 3
                tmp += int(tn[j])
            tns.add(tmp)
            tn[i] = '2'
            tmp = 0
            for j in range(len(tn)):
                tmp *= 3
                tmp += int(tn[j])
            tns.add(tmp)

            tn[i] = '1'
        else:
            tn[i] = '0'
            tmp = 0
            for j in range(len(tn)):
                tmp *= 3
                tmp += int(tn[j])
            tns.add(tmp)
            tn[i] = '1'
            tmp = 0
            for j in range(len(tn)):
                tmp *= 3
                tmp += int(tn[j])
            tns.add(tmp)

            tn[i] = '2'
    print('#{} {}'.format(t, bns.intersection(tns).pop()))