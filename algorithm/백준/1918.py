'''
우선순위 오름차순
(
+-
*/
)
이다.
우선순위 낮은 연산자를 만날 때까지 pop을 하면서 출력을 하면 된다.
'''

d = {
    ')': 0,
    '(': 1,
    '+': 2,
    '-': 2,
    '*': 3,
    '/': 3,
}
pre = input() + ')'
st = ['(']
r = []
for s in pre:
    if s != '(':
        while st and d.get(st[-1], 4) >= d.get(s, 4):
            tmp = st.pop()
            if tmp != '(':
                r.append(tmp)
            else:
                break
    if s != ')':
        st.append(s)

print(''.join(r))