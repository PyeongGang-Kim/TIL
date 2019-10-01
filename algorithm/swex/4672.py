'''
주어진 인풋을 순서를 바꿔서 연속적인 부분문자열들을 구할 수 있다.
펠린드롬이 최대한이 되기 위해선 같은 문자끼리 붙여줘야 한다.
=> 인풋받은 데이터를 정렬한다.
==> 펠린드롬의 갯수를 센다
'''
T = int(input())
for t in range(1, T+1):
    a = ''.join(sorted(list(input())))
    R = 0
    tmp = []
    for i in range(1, len(a)+1):
        for j in range(len(a)-i+1):
            tmp.append(a[j:j+i])
    for w in tmp:
        chk = True
        for c in range(len(w)//2):
            if w[c] != w[-1-c]:
                chk = False
                break
        if chk:
            R += 1

    print('#{} {}'.format(t, R))