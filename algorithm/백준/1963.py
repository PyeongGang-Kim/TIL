'''
하나씩 바꾼 것들 다 저장 cnt 1
cnt 1의 값들을 다시 한번만 바꿔서 저장
저장할 때마다 이미 한 것들은 저장하지 않기
각 단계마다 셋 만들고 다음단계 넘어갈 때 방문리스트를 업데이트한다.

'''
def solve(a, cnt=0):
    global r, tmpset
    while 1:

        tmpset2 = set()
        for s in tmpset:
            b = list(s)
            for i in nl2:
                b[0] = str(i)
                tmp = ''.join(b)
                if PRIME[int(tmp)] and tmp not in tmpset:
                    if tmp == B:
                        r = cnt + 1
                        return
                    tmpset2.add(tmp)
            for j in range(1, 4):
                b = list(s)
                for i in nl1:
                    b[j] = str(i)
                    tmp = ''.join(b)
                    if PRIME[int(tmp)] and tmp not in tmpset:
                        if tmp == B:
                            r = cnt + 1
                            return
                        tmpset2.add(tmp)
        if tmpset2:
            cnt += 1
            tmpset.update(tmpset2)
        else:
            return


nl1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
nl2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

PRIME = [True for _ in range(10000)]
for i in range(2, 5000):
    if PRIME[i]:
        for j in range(i*2, 10000, i):
            PRIME[j] = False


T = int(input())
for t in range(T):
    A, B = input().split()
    if A == B:
        print(0)
    else:
        a = list(A)
        b = list(B)
        r = 0xffffffff
        tmpset = {A}
        solve(a)
        if r == 0xffffffff:
            print('IMPOSSIBLE')
        else:
            print(r)