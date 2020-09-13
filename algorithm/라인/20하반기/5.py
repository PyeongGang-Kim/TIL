def cardsum(cur_cards):
    # 1을 제외한 모든 카드 더한다. 1은 갯수만 센다.
    cnt = 0
    cnt2 = 0
    for card in cur_cards:
        if card != 1:
            cnt += card
        else:
            cnt2 += 1
    # 최대값을 반환
    if cnt2:
        if cnt + cnt2 + 10 < 22:
            return cnt + cnt2 + 10
        return cnt + cnt2
    return cnt


def game(cards):
    global cnt, card_index
    # 카드 꺼낼때마다 꺼낼 수 있는지 확인 후 못꺼내면 false 반환하기
    if card_index == len(cards):
        return False
    pc = [min(10, cards[card_index])]
    card_index += 1
    if card_index == len(cards):
        return False
    dc = [min(10, cards[card_index])]
    card_index += 1
    if card_index == len(cards):
        return False
    pc.append(min(10, cards[card_index]))
    card_index += 1
    if card_index == len(cards):
        return False
    dc.append(min(10, cards[card_index]))
    card_index += 1
    # 초기세팅 완료 블랙잭 확인
    if cardsum(pc) == 21:
        if cardsum(dc) == 21:
            return True
        cnt += 3
        return True

    # 플레이어 카드받기 시작
    while 1:
        if dc[0] == 1 or dc[0] > 6:
            # 17 이상 될 때까지 받아야한다.
            if cardsum(pc) > 16:
                break
            if card_index == len(cards):
                return False
            pc.append(min(10, cards[card_index]))
            card_index += 1
        elif dc[0] == 2 or dc[0] == 3:
            # 12 이상이 될 때까지 받아야한다.
            if cardsum(pc) > 11:
                break
            if card_index == len(cards):
                return False
            pc.append(min(10, cards[card_index]))
            card_index += 1
        else:
            # 받지 않는다.
            break
    # 21 초과 시 패배
    pcs = cardsum(pc)
    if pcs > 21:
        cnt -= 2
        return True
    # 플에이어 카드 받기 종료 딜러 카드 받기 시작
    while 1:
        if cardsum(dc) > 16:
            break
        if card_index == len(cards):
            return False
        dc.append(min(10, cards[card_index]))
        card_index += 1
    # 21 초과 시 승리
    dcs = cardsum(dc)
    if dcs > 21:
        cnt += 2
        return True
    # 딜러 카드 받기 종료 승 패 비교
    if pcs > dcs:
        cnt += 2
    elif pcs == dcs:
        pass
    else:
        cnt -= 2

    # 게임 종료
    return True


def solution(cards):
    global cnt, card_index
    cnt = 0
    card_index = 0
    # 게임이 가능한동안 계속 진행
    while game(cards):
        continue

    answer = cnt
    return answer

print(solution([12, 7, 11, 6, 2, 12]))