def chk(sx, sy, ex, ey, arr):
    if sx == ex:
        return False
    tmp = arr[sy][sx]
    for j in range(sy, ey):
        for i in range(sx, ex):
            if arr[j][i] != tmp:
                return False
    return True


def qurd(sx, sy, ex, ey, arr):
    if not chk(sx, sy, ex, ey, arr):
        mx, my = (sx + ex) >> 1, (sy + ey) >> 1
        if mx == sx:
            t0, t1 = 0, 0
            for j in range(sy, ey):
                for i in range(sx, ex):
                    if arr[j][i]:
                        t1 += 1
                    else:
                        t0 += 1
            print(sx, ex, sy, ey, 100)
            return t0, t1
        num0, num1 = 0, 0
        t0, t1 = qurd(sx, sy, mx, my, arr)
        num0 += t0
        num1 += t1
        t0, t1 = qurd(mx, sy, ex, my, arr)
        num0 += t0
        num1 += t1
        t0, t1 = qurd(sx, my, mx, ey, arr)
        num0 += t0
        num1 += t1
        t0, t1 = qurd(mx, my, ex, ey, arr)
        num0 += t0
        num1 += t1
        return num0, num1
    if arr[sy][sx]:
        return 0, 1
    return 1, 0


def solution(arr):

    answer = list(qurd(0, 0, len(arr), len(arr), arr))
    print(answer)
    return answer
solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]])