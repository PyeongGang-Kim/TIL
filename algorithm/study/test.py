import sys
input = sys.stdin.readline

'''
민 세그
첫번째 시험 오름차순 정렬
세그 좌표는 두번째 시험 순
거기에 들어가는 값은 세번째 성적
성적을 넣을 때마다 세그 업데이트하기

나보다 작은 2번째 구간의 최소값이 3번째보다 크면
나는 굉장한 학생이 된다.



 Input
3 
2 3 1
3 1 2
1 2 3

 Output
 3
Note: No contestant is better than any other contestant, hence all three are excellent.

 Input
10 
2 5 3 8 10 7 1 6 9 4
1 2 3 4 5 6 7 8 9 10
3 8 7 10 5 4 1 2 6 9

 Output
 4
Note: The excellent contestants are those numbered with 1, 2, 3 and 5.
'''
def seg(s, e, idx = 1):
    if pos <= s:
        return 500001
    if pos > e:
        return tree[idx]
    m = (s + e) // 2
    idx <<= 1
    return min(seg(s, m, idx), seg(m+1, e, idx+1))


N = int(input())
cnt = 0
N2 = 2
while N2 < N:
    N2 <<= 1
offset = N2 - 1
N2 <<= 1
tree = [500001] * N2
nl = [[0, 0, 0] for _ in range(N)]
for i in range(3):
    for idx, num in enumerate(map(int, input().split())):
        nl[num-1][i] = idx
nl.sort()
i = 0
while i < N:
    pos = nl[i][1]
    val = nl[i][2]
    if seg(0, offset) > nl[i][2]:
        cnt += 1
    i += 1
    tmp = offset + pos + 1
    tree[tmp] = val
    tmp >>= 1
    while tmp:
        t1 = tmp << 1
        t2 = t1 + 1
        tree[tmp] = min(tree[t1], tree[t2])
        tmp >>= 1

print(cnt)
