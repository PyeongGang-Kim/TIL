from collections import deque


def convtime(time):
    return int(time[:2]) * 3600 + int(time[3:5]) * 60 + int(time[6:])


def solution(play_time, adv_time, logs):
    # 시간을 숫자로 변경
    play_time = convtime(play_time)
    adv_time = convtime(adv_time)
    answer = ''
    # 총 시간만큼의 배열을 생성한다.
    nl = [0] * (play_time)

    # 들어가는 리스트 하나 나가는 리스트 하나 각 생성
    inlist = []
    outlist = []
    for log in logs:
        inlist.append(convtime(log.split("-")[0]))
        outlist.append(convtime(log.split("-")[1]))
    inlist = deque(sorted(inlist))
    outlist = deque(sorted(outlist))

    # 각 시간별로 순차적으로 실행한다.
    # 1씩 증가해가면서 두 리스트 비교한다. 이상이 되면 아닐때까지 팝하면서 갯수 제외한다.
    cnt = 0
    for i in range(play_time):
        while inlist and inlist[0] <= i:
            cnt += 1
            inlist.popleft()
        while outlist and outlist[0] <= i:
            cnt -= 1
            outlist.popleft()
        nl[i] = cnt
    # 첫 시간구간부터 재생시간만큼 슬라이딩윈도우 적용하면서 최대값 찾기
    cur = 0
    for i in range(adv_time):
        cur += nl[i]

    tmp = 0
    maxnum = cur
    for i in range(play_time - adv_time):
        cur += nl[i + adv_time]
        cur -= nl[i]
        if cur > maxnum:
            maxnum = cur
            tmp = i + 1

    # 최대 시간 찾았으면 문자로 변환하기
    # answer = "{}:{}:{}".format(tmp//3600, tmp//60, )
    t1 = str(tmp // 3600)
    tmp %= 3600
    t2 = str(tmp // 60)
    tmp %= 60
    t3 = str(tmp)
    if len(t1) == 1:
        t1 = '0' + t1
    if len(t2) == 1:
        t2 = '0' + t2
    if len(t3) == 1:
        t3 = '0' + t3
    print(nl)
    return "{}:{}:{}".format(t1, t2, t3)

print(
solution("00:00:05", "00:00:03", ["00:00:00-00:00:04", "00:00:01-00:00:04", "00:00:04-00:00:05", "00:00:04-00:00:05", "00:00:04-00:00:05"])
)