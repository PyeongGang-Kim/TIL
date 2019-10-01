'''
10의 자리일 경우 4가 나오는 횟수 1번
세자리 일 경우(100) 4가 나오는 횟수 19번
((   1번*9(4, 14,,, 94) + 10(40, 41,,, 49)   ))
네자리 일 경우(1000)
((   100의 자리 경우의 수 19번 * 9 + 100(400, 401,,, 499)
계속 반복됨.

589 일 경우
500, 80, 9 이렇게 각 자리수별로 나눠서 계산한 값들을 더해주면 된다.
각 자리수들에 대해서
맨 앞의 숫자가 i일 때
i < 4이면 이전자리수 최대값 * i
i > 4이면 이전자리수 최대값 * (i - 1) + 10 ** ( 현재 자리수 - 1)
뒤의 층에 앞의 층을 빼 준다.
0층이 없으므로 입력받은 숫자의 부호가 다를 경우 층을 하나 더 빼준다.

'''


T = int(input())
for t in range(1, T+1):
    a, b = input().split()
    c1, c2 = 1, 1
    if a[0] == '-':
        a = a[1:]
        c1 = -1
    if b[0] == '-':
        b = b[1:]
        c2 = -1
    r2 = 0
    for i in range(len(a)):
        if a[i] != '0':
            tmp = len(a)-i
            n = 0
            nn = 0
            while tmp > 1:
                n = n*9 + 10**nn
                nn += 1
                tmp -= 1
            if int(a[i]) < 4:
                r2 += n*int(a[i])
            else:
                r2 += n*(int(a[i])-1) + (10**(len(a)-i-1))
    r3 = 0
    for i in range(len(b)):
        if b[i] != '0':
            tmp = len(b) - i
            n = 0
            nn = 0
            while tmp > 1:
                n = n * 9 + 10 ** nn
                nn += 1
                tmp -= 1
            if int(b[i]) < 4:
                r3 += n * int(b[i])
            else:
                r3 += n * (int(b[i]) - 1) + (10 ** (len(b) - i - 1))
    r = (int(b)-r3)*c2 - (int(a)-r2)*c1
    if c1 != c2:
        r -= 1
    print('#{} {}'.format(t, r))