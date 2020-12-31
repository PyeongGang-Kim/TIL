import sys
sys.setrecursionlimit(10000000000)


def solve(L, W, H):
    if not (L and W and H):
        return True
    cs = min(L, W, H)
    while cs:
        idx = cs & (cs - 1)
        if not idx:
            break
        cs = idx
    idx = 0
    while idx < 21:
        if cs & (1 << idx):
            break
        idx += 1


    # 인덱스 알았으니 여기서부터 줄여가면서 확인할 것.
    num = 1
    while num:
        if nl[idx]:
            if nl[idx] < num:
                num -= nl[idx]
                nl[idx] = 0
            else:
                nl[idx] -= num
                num = 0
        if not idx:
            break
        num <<= 3

        if num > (1 << 50):
            break
        idx -= 1

    # num이 남아있으면 실패한것임.
    if num:
        return False

    # num이 없으면 남은 상자들로 확인한다.
    if not solve(L, W, H-cs):
        return False
    if not solve(L-cs, W, cs):
        return False
    if not solve(cs, W-cs, cs):
        return False
    return True


L, W, H = map(int, input().split())
n = int(input())
nl = [0] * 21

while n:
    n -= 1
    a, b = map(int, input().split())
    nl[a] = b
r = sum(nl)
print(r-sum(nl) if solve(L, W, H) else -1)
print(nl)