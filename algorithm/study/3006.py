import sys
input = sys.stdin.readline
'''
수들의 인덱스를 기준으로 조회를 하면 된다.

front, rear 두개 사용
front, rear 숫자가 담겨 있는 곳의 인덱스의 성분이 몇번이나 더해졌는지 확인할 수 있으면 된다.

'''
def seg(s, e, pos, idx=1):
    if s == e:
        if s == pos:
            return tree[idx]
        return 0
    if s <= pos <= e:
        m = (s + e) // 2
        idx <<= 1
        return seg(s, m, pos, idx) + seg(m+1, e, pos, idx+1) + tree[idx >> 1]
    return 0


def update1(s, e, pos, idx=1):
    if pos > e:
        tree[idx] += 1
        return
    if s < pos:
        idx <<= 1
        m = (s + e) // 2
        update1(s, m, pos, idx)
        update1(m + 1, e, pos, idx + 1)
    return


def update2(s, e, pos, idx=1):
    if s > pos:
        tree[idx] -= 1
        return
    if pos < e:
        idx <<= 1
        m = (s + e) // 2
        update2(s, m, pos, idx)
        update2(m + 1, e, pos, idx + 1)
    return


N = int(input())
N2 = 2
while N2 < N:
    N2 <<= 1
N2 <<= 1
nl = [int(input()) for _ in range(N)]
tree = [0 for _ in range(N2)]
idxl = [0 for _ in range(N)]
i = 0
idx = N2 >> 1
while N:
    idxl[nl[i]-1] = i
    tree[idx] = i
    N -= 1
    i += 1
    idx += 1
front = 0
rear = i - 1
N = (N2 >> 1) - 1
r = []
i = 1
while front <= rear:
    if i & 1:
        #idxl[i] 인덱스에서 세그 탐색 실행
        r.append(str(seg(0, N, idxl[front]) - front))
        #nl[i] 인덱스보다 작은 곳에 다 더해주기
        update1(0, N, idxl[front])
        front += 1
    else:
        #idxl[i] 인덱스에서 세그 탐색 실행
        r.append(str(rear - seg(0, N, idxl[rear])))
        #nl[i] 인덱스보다 큰 곳에 다 빼주기
        update2(0, N, idxl[rear])
        rear -= 1
    i += 1
print('\n'.join(r))