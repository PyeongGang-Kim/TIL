'''

맨 끝에서부터 첫번재까지 순차적으로.
현재 인덱스의 탑 높이를 스택에 넣는다.
다음 탑 높이를 본 후(탑의 높이가 같은 경우는 없으므로)
스택의 맨 위의 값이 더 높아질 때 까지 스택의 탑을 빼 준다.
빠진 탑들은 내가 비교한 탑에서 신호를 수신할 수 있다.
나보다 낮으면 넘어간다.

'''
N = int(input())
nl = list(map(int, input().split()))
st = []
vl = ['0' for _ in range(len(nl))]
for i in range(len(nl)-1, 0, -1):
    st.append((nl[i], i))
    while st and nl[i-1] > st[-1][0]:
        tmp = st.pop()
        vl[tmp[1]] = str(i)
print(' '.join(vl))

