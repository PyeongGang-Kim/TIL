import sys
sys.stdin = open("4861회문_input.txt")

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().strip().split(' '))
    tempList = [list(input().strip()) for n in range(N)]
    chk = 0
    tempWord = []
    for n in range(N):
        for m in range(N-M+1):
            tempWord = tempList[n][m:m+M]
        if tempWord == tempWord[::-1]:
            chk += 1
            break
    if not chk:
        for mm in range(N):
            if not chk:
                for i in range(N-M+1):
                    tempWord = []
                    for m in range(M):
                        tempWord.append(tempList[m+i][mm])
                    if tempWord == tempWord[::-1]:
                        chk += 1
                        break
    print('#{} {}'.format(t, ''.join(tempWord)))