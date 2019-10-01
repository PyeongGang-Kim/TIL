'''
각 자리의 숫자와 영문자가 일치하는지 확인하기 위하여
각각의 영문자를 숫자값으로 변환해주는 딕셔너리를 만든다.
문자를 순차적으로 탐색하며 비교하면 해결.
'''


T = int(input())
for t in range(1, T+1):
    S, N = input().split()
    wl = input().split()
    di = {
        'a': '2', 'b': '2', 'c': '2', 'd': '3', 'e': '3', 'f': '3',
        'g': '4', 'h': '4', 'i': '4', 'j': '5', 'k': '5', 'l': '5',
        'm': '6', 'n': '6', 'o': '6', 'p': '7', 'q': '7', 'r': '7',
        's': '7', 't': '8', 'u': '8', 'v': '8', 'w': '9', 'x': '9',
        'y': '9', 'z': '9'
          }
    r = 0
    for word in wl:
        chk = False
        for i, w in enumerate(word):
            if S[i] != di[w]:
                chk = True
                break
        if not chk:
            r += 1
    print('#{} {}'.format(t, r))