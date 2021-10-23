# 쌓고 넣은 경우
# 안쌓고 넣은 경우
# 두가지에 대해서 반환받은 경우의 수를 합쳐서 반환하기

st = [0 for _ in range(200009)]
sti = -1

def dfs(i, a):
    global n, sti
    x = 0
    y = 0
    # 두개가 쌓여 있는 상태에서
    # 합칠 수 있다면 합쳐본다.
    if sti > 0:
        if st[sti] == st[sti-1]:
            t = st[sti]
            st[sti-1] += st[sti]
            sti -= 1
            x = dfs(i, a) + 1
            st[sti] -= t
            sti += 1
            st[sti] = t
    i += 1
    if i == n:
        return x
    # 한칸 전진
    sti += 1
    st[sti] = a[i]
    # 안합친 경우의 수도 확인해본다.
    y = dfs(i, a)
    sti -= 1
    return x + y


def solution(a, s):
    global n, st, sti
    si = 0

    for i in range(1, len(s)):
        s[i] += s[i - 1]
    cur = 0

    answer = []
    for ss in s:
        # 실행 cur 부터 ss까지 실행
        n = ss
        sti += 1
        st[sti] = a[cur]
        answer.append(dfs(cur, a)+1)
        sti -= 1
        cur = ss
    return answer

print(solution([1,1,1,1,1,1,2,5,8,2,1,1,4,8,8,8,12,6,6], [4,3,1,5,6]))