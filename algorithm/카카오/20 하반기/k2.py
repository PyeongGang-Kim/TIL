def comb(cur_len, cur_index, to_len, cur_text=""):
    # t2를 가지고 2, 3, ... len(t2)의 조합 만들어주기
    # 선택했냐 안했냐 원하는 갯수냐에 따라 추가할 것.
    if cur_index == to_len:
        return
    comb(cur_len, cur_index + 1, to_len, cur_text)
    if len(cur_text) + 1 in course_set:
        combis.add(cur_text + t2[cur_index])
    comb(cur_len, cur_index + 1, to_len, cur_text + t2[cur_index])


def solution(orders, course):
    global t2
    # 메뉴들 전부 확인해서 2번 이상 주문된 요리만 남긴다.
    # 이 모든 메뉴를 가지고 2개 이상의 조합들을 만든다.
    # 만들어진 조합을 모든 오더랑 비교한다.

    # 셋에 있는지 확인 있으면 다음셋에 추가하기 없으면 현재셋에만 추가하기
    t1 = set()
    t2 = set()
    for order in orders:
        for menu in order:
            if menu in t1:
                t2.add(menu)
            else:
                t1.add(menu)
    t2 = sorted(list(t2))

    global combis
    combis = set()

    global course_set
    course_set = set(course)
    comb(0, 0, len(t2))
    print(combis)
    print(orders)

    course = {k: [] for k in course}
    course2 = [2 for _ in range(11)]

    # 각 코스길이 별로 코스를 추가해야 한다.
    # 각 코스길이마다 최대 카운팅을 추가로 구성
    # 최대 카운팅과 같으면 추가
    # 최대 카운팅보다 크면 초기화 후 추가

    for combi in combis:
        # 각 코스별로 몇개의 오더에 들어갔는지 확인
        cnt = 0
        for order in orders:
            chk = len(combi)
            for menu in combi:
                if menu in order:
                    chk -= 1
            if not chk:
                cnt += 1
        # 현재 combi의 길이에 맞는 최대값 확인
        if course2[len(combi)] == cnt:
            course[len(combi)].append(combi)
        elif course2[len(combi)] < cnt:
            course[len(combi)] = [combi]
            course2[len(combi)] = cnt
    answer = []
    for k, v in course.items():
        for vv in v:
            answer.append(vv)
    return sorted(list(answer))

# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))