def solve(a, b):
    # 종료조건 - a, b 둘 다 0인 경우이다.
    if not (a|b):
        return 1
    tmp = 0
    if a < b:
        if a:
            tmp += solve(a-1, b)
        tmp += solve(a, b-1)
    elif a == b:
        tmp += solve(a-1, b)
    else:
        return 0
    return tmp


def solution(n):
    answer = solve(n, n)
    return answer


# print(solution(3))