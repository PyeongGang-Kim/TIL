'''

아직 정답이 나오지 않은 코드
'''


def sol(sales, i):
    if cl[i]:
        # 이미 방문했으면 방문할지 말지 선택 가능
        if nl[i]:
            tmp = 0
            for k in nl[i]:
                tmp += sol(sales, k)
            if tmp < sales[i]:
                return tmp
            else:
                return sales[i]
        else:
            return 0
    else:
        # 무조건 방문해야함
        cl[i] = 1
        # 자식과 부모 모두 방문처리하고 비용을 합한다.
        cost = sales[i]
        for k in nl[i]:
            cl[k] = 1
            cost += sol(sales, k)
            cl[k] = 0
        return cost


def solution(sales, links):
    # 이미 간 적이 있다면 자신이 갈 것인지 팀원이 갈 것인지 판단해야 한다. 지금 내 매출과 자식들 매출 합의 최소값에 따라 결정한다.
    # 간 적이 없다면 무조건 참석
    global cl, nl

    # 1번부터 n명까지의 가치
    # 각 노드별로 자식을 알아야한다.
    # 각 노드는 자식을 리스트로 가진다.
    nl = [[] for _ in range(len(sales))]
    for link in links:
        a, b = link
        nl[a - 1].append(b - 1)
    cl = [0] * len(nl)
    print(nl)
    answer = sol(sales, 0)

    return answer

print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17], [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))