nl = [0] * 100001


def solution(boxes):
    # 모든 제품 제품 별 카운팅해야함, 같은 상자인거 나올 때 2개씩 빼야 함
    # 총 박스 개수 - 짝수로 채울 수 있는 개수만큼 구매하면 된다.

    # 각 박스별로 있으면 카운팅+1 후 없애주기
    cnt = 0
    for box in boxes:
        for item in box:
            if nl[item]:
                nl[item] = 0
                cnt += 1
            else:
                nl[item] = 1

    answer = len(boxes) - cnt
    return answer