lans = ["cpp", "java", "python"]
poss = ["backend", "frontend"]
wls = ["junior", "senior"]
foods = ["chicken", "pizza"]

def bs(s, e, score_list, num):
    if s == e:
        return s
    m = (s + e)>>1
    # 오른쪽 구간 가야하는 경우
    if score_list[m] < num:
        return bs(m+1, e, score_list, num)
    else:
        # 왼쪽 구간 선택해야 하는 경우
        return bs(s, m, score_list, num)



def ins1(query):
    if query[0] == "-":
        for lan in lans:
            ins2(query, TREE[lan])
    else:
        ins2(query, TREE[query[0]])


def ins2(query, suq):
    if query[1] == "-":
        for pos in poss:
            ins3(query, suq[pos])
    else:
        ins3(query, suq[query[1]])


def ins3(query, suq):
    if query[2] == "-":
        for wl in wls:
            ins4(query, suq[wl])
    else:
        ins4(query, suq[query[2]])


def ins4(query, suq):
    if query[3] == "-":
        for food in foods:
            suq.append(query[4])
    else:
        suq[query[3]].append(int(query[4]))

def cal1(query):
    cnt = 0
    if query[0] == "-":
        for lan in lans:
            cnt += cal2(query, TREE[lan])
    else:
        cnt += cal2(query, TREE[query[0]])
    return cnt

def cal2(query, suq):
    cnt = 0
    if query[2] == "-":
        for pos in poss:
            cnt += cal3(query, suq[pos])
    else:
        cnt += cal3(query, suq[query[2]])
    return cnt

def cal3(query, suq):
    cnt = 0
    if query[4] == "-":
        for wl in wls:
            cnt += cal4(query, suq[wl])
    else:
        cnt += cal4(query, suq[query[4]])
    return cnt

def cal4(query, suq):
    cnt = 0
    if query[6] == "-":
        for food in foods:
            score_list = suq[food]
            cnt += len(score_list) - bs(0, len(score_list), score_list, query[7])
    else:
        score_list = suq[query[6]]
        cnt = len(score_list) - bs(0, len(score_list), score_list, query[7])
    return cnt

def solution(info, query):
    global TREE
    TREE = dict()

    for lan in lans:
        TREE[lan] = dict()
        for pos in poss:
            TREE[lan][pos] = dict()
            for wl in wls:
                TREE[lan][pos][wl] = dict()
                for food in foods:
                    TREE[lan][pos][wl][food] = []

    for inf in info:
        ins1(inf.split(" "))
    # 삽입 다 끝나면 정렬 후 이분탐색
    for lan in lans:
        for pos in poss:
            for wl in wls:
                for food in foods:
                    TREE[lan][pos][wl][food].sort()
    # 0, 2, 4, 6, 7
    answer = []
    for quer in query:
        quer = quer.split(" ")
        quer[7] = int(quer[7])
        answer.append(cal1(quer))
    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])
