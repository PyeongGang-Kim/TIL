# 0번집이 털린 경우의 dp 최대값 - 마지막 빼고 할것
# 0번집이 털리지 않은 경우의 dp 최대값 - 첫번째 빼고 할 것


def solution(money):
    D11 = [0] * len(money)
    D12 = [0] * len(money)
    D21 = [0] * len(money)
    D22 = [0] * len(money)

    D11[0] = money[0]
    D21[1] = money[1]
    # 이전 인덱스의 0 번이 털린경우의 최대값
    # 1번이 털리지 않은 경우의 최대값
    for i in range(1, len(money) - 1):
        D11[i] = money[i] + D12[i-1]
        D12[i] = D11[i-1] if D11[i-1] > D12[i-1] else D12[i-1]
    for i in range(2, len(money)):
        D21[i] = money[i] + D22[i-1]
        D22[i] = D21[i-1] if D21[i-1] > D22[i-1] else D22[i-1]

    answer = max(D11[-2], D12[-2], D21[-1], D22[-1])

    return answer
print(solution([1, 2, 3, 1]	))