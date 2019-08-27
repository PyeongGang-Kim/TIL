import sys
sys.stdin = open('Forth_input.txt')

results = []
T = int(input())
for t in range(1, T+1):
    st = []
    s = input().split()
    try:
        for ss in s:
            if ss.isnumeric():
                st.append(int(ss))
            elif ss == '.':
                if len(st) == 1:
                    result = '#{} '.format(t) + str(st.pop())
                else:
                    result = '#{} '.format(t) + 'error'
            else:
                t1, t2 = st.pop(), st.pop()
                if ss == '+':
                    st.append(t2 + t1)
                elif ss == '-':
                    st.append(t2 - t1)
                elif ss == '*':
                    st.append(t2 * t1)
                elif ss == '/':
                    st.append(t2 // t1)
    except:
        result = '#{} '.format(t) + 'error'

    results.append(result)
print('\n'.join(results))
