import sys
sys.stdin = open('괄호검사.txt')


T = int(input())
for t in range(1, T+1):
    S = input()
    nl = []
    result = 1
    for s in S:
        if s in '{(':
            nl.append(s)
        elif s in '})':
            if nl:
                if nl[-1] == '{' and s == '}':
                    nl.pop()
                elif nl[-1] == '(' and s == ')':
                    nl.pop()
                else:
                    result = 0
                    break
            else:
                result = 0
                break
    if nl:
        result = 0

    print('#{} {}'.format(t, result))
