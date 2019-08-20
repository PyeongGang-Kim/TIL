import sys
sys.stdin = open("4864문자열비교_input.txt")

T = int(input())
for t in range(1, T+1):
    A = input()
    jump = list(range(len(A), 0, -1))
    B = input()
    num = 0

    i=0
    for b in B:
        if i+len(A) > len(B):
            break
        jumpchk = 0
        D=B[i:i+len(A)]
        for k, a in enumerate(A):
            if a not in D:
                i += jump[k]
                jumpchk = 1
                break
        if jumpchk == 0:
            i += 1
            if A == D:
                num += 1

    print('#{} {}'.format(t, num))