def solution(balls, order):
    answer = []
    # 명령이 있어도 못빼는 경우에는 내 양옆인덱스 값을 키로 가지는 딕셔너리에 각 각 추가해준다.
    # 각 숫자 별 공의 위치를 파악이 필요함
    # 공이 빠질 때 딕셔너리 조회한 후 빠진여부 체크해서 안빠졌으면 빼 준다.
    # 왼쪽 인덱스 i 오른쪽 인덱스 j

    il = [0] * 1000001
    for i, ball in enumerate(balls):
        il[ball] = i
    i = 0
    j = len(balls) - 1

    # 오른쪽을 뺄 수 있는 chk_dict1
    # 왼쪽을 뺄 수 있는 chk_dict2
    chk_dict1 = dict()
    chk_dict2 = dict()
    chk_set = set()
    k = 0
    while i <= j and k != len(order):
        tmp = order[k]
        k += 1
        # 뺄 수 있으면 바로 뺀다 빼고 나서 뺄수있는것들 다 확인해준다.
        if balls[i] == tmp or balls[j] == tmp:
            if balls[i] == tmp:
                tmp2 = balls[i]
                answer.append(balls[i])
                i += 1
                while chk_dict1.get(tmp2):
                    if chk_dict1[tmp2] not in chk_set:
                        chk_set.add(chk_dict1[tmp2])
                        answer.append(chk_dict1[tmp2])
                        tmp3 = chk_dict1[tmp2]
                        del chk_dict1[tmp2]  #### 삭제 가능?
                        tmp2 = tmp3
                        i += 1
                    else:
                        break
            else:
                tmp2 = balls[j]
                answer.append(balls[j])
                j -= 1
                while chk_dict2.get(tmp2):
                    if chk_dict2[tmp2] not in chk_set:
                        chk_set.add(chk_dict2[tmp2])
                        answer.append(chk_dict2[tmp2])
                        tmp3 = chk_dict2[tmp2]
                        del chk_dict2[tmp2]
                        tmp2 = tmp3
                        j -= 1
                    else:
                        break
        else:
            # tmp의 인덱스 조회해서 양 옆의 값을 확인해야 한다.
            tiv = balls[il[tmp] - 1]
            tjv = balls[il[tmp] + 1]
            # 두 개의 값들이 이미 빠졌는지 확인 후 안빠졌으면 각 각 추가해줄 것
            if tiv not in chk_set:
                chk_dict1[tiv] = tmp
            if tjv not in chk_set:
                chk_dict2[tjv] = tmp

    return answer

# print(solution([1,2,3,4,5,6], [6,2,5,1,4,3]))
print(solution([11, 2, 9, 13, 24], [9, 2, 13, 24, 11]))