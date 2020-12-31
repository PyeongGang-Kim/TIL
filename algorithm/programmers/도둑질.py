# 0번집이 털린 경우의 dp 최대값 - 마지막 빼고 할것
# 0번집이 털리지 않은 경우의 dp 최대값 - 첫번째 빼고 할 것


def solution(money):
    D1 = [[0 for _ in range(2)] for _ in range(len(money))]
    D2 = [[0 for _ in range(2)] for _ in range(len(money))]

    D1[0][0] = money[0]
    D2[1][0] = money[1]
    # 이전 인덱스의 0 번이 털린경우의 최대값
    # 1번이 털리지 않은 경우의 최대값
    for i in range(1, len(money) - 1):
        D1[i][0] += money[i] + D1[i-1][1]
        D1[i][1] = max(D1[i-1])
    for i in range(2, len(money)):
        D2[i][0] += money[i] + D2[i-1][1]
        D2[i][1] = max(D2[i-1])

    answer = max(max(D1[-2]), max(D2[-1]))

    return answer
# print(solution([1, 2, 3, 1]	))