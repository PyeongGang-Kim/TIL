import sys
sys.stdin = open('반복문자지우기.txt')

T = int(input())
for t in range(1, T+1):
    S = list(input())
    i = 0
    while i < len(S)-1:
        if i < 0 :
            i = 0
        if S[i] == S[i+1]:
            S.pop(i)
            S.pop(i)
            i -= 2
        i += 1
    print('#{} {}'.format(t, len(S)))