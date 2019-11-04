D = [[], [1, 0], [-1, 0], [0, -1], [0, 1]]
N, K = map(int, input().split())
nl = [list(map(int, input().split())) for _ in range(N)]
dl = []
dp = set()
for k in range(K):
    y, x, d = map(int, input().split())
    dl.append([x, y, [d]])
    dp.add((x, y))
tim = 0
cnt = 1
while tim < 1000:
    # 드론들 순번대로 이동한다
    delli = []
    for i in range(len(dl)):
        x, y = dl[i][0], dl[i][1]
        d = dl[i][2]
        tx, ty = x + D[d][0], y + D[d][1]
        if 0 <= tx < N and 0 <= ty < N:
            # 빨간색
            if nl[ty][tx] == 1:
                if (tx, ty) in dp:
                    for j in range(len(dl)):
                        if dl[j][0] == tx and dl[j][1] == ty:
                            dl[j][2].append(reversed(dl[i][2]))
                            cnt = max(cnt, len(dl[j][2]))
                            delli.append(i)
                            break
                else:
                    dp.remove((x, y))
                    dp.add((tx, ty))
                    dl[i][0] = tx
                    dl[i][1] = ty
            # 파란색
            elif nl[ty][tx] == 2:
                tx2, ty2 = x - D[d][0], y - D[d][1]
                if 0 <= tx2 < N and 0 <= ty2 < N:
                    # 빨간색
                    if nl[ty2][tx2] == 1:
                        if (tx2, ty2) in dp:
                            for j in range(len(dl)):
                                if dl[j][0] == tx2 and dl[j][1] == ty2:
                                    dl[j][2].append(reversed(dl[i][2]))
                                    cnt = max(cnt, len(dl[j][2]))
                                    delli.append(i)
                                    break
                        else:
                            dp.remove((x, y))
                            dp.add((tx2, ty2))
                            dl[i][0] = tx2
                            dl[i][1] = ty2
                    # 파란색
                    elif nl[ty2][tx2] == 2:
                        if dl[i][2][0] == 1:
                            dl[i][2][0] = 2
                        elif dl[i][2][0] == 2:
                            dl[i][2][0] = 1
                        elif dl[i][2][0] == 3:
                            dl[i][2][0] = 4
                        else:
                            dl[i][2][0] = 3
                    # 흰색
                    else:
                        if (tx, ty) in dp:
                            for j in range(len(dl)):
                                if dl[j][0] == tx and dl[j][1] == ty:
                                    dl[j][2].append(reversed(dl[i][2]))
                                    cnt = max(cnt, len(dl[j][2]))
                                    delli.append(i)
                                    break
                        else:
                            dp.remove((x, y))
                            dp.add((tx, ty))
                            dl[i][0] = tx
                            dl[i][1] = ty
                # 파란색
                else:
                    if dl[i][2][0] == 1:
                        dl[i][2][0] = 2
                    elif dl[i][2][0] == 2:
                        dl[i][2][0] = 1
                    elif dl[i][2][0] == 3:
                        dl[i][2][0] = 4
                    else:
                        dl[i][2][0] = 3
            # 흰색
            else:
                if (tx, ty) in dp:
                    for j in range(len(dl)):
                        if dl[j][0] == tx and dl[j][1] == ty:
                            dl[j][2].append(reversed(dl[i][2]))
                            cnt = max(cnt, len(dl[j][2]))
                            delli.append(i)
                            break
                else:
                    dp.remove((x, y))
                    dp.add((tx, ty))
                    dl[i][0] = tx
                    dl[i][1] = ty
        # 파란색
        else:
            tx2, ty2 = x - D[d][0], y - D[d][1]
            if 0 <= tx2 < N and 0 <= ty2 < N:
                # 빨간색
                if nl[ty2][tx2] == 1:
                    if (tx2, ty2) in dp:
                        for j in range(len(dl)):
                            if dl[j][0] == tx2 and dl[j][1] == ty2:
                                dl[j][2].append(reversed(dl[i][2]))
                                delli.append(i)
                                break
                    else:
                        dp.remove((x, y))
                        dp.add((tx2, ty2))
                        dl[i][0] = tx2
                        dl[i][1] = ty2
                # 파란색
                elif nl[ty2][tx2] == 2:
                    if dl[i][2][0] == 1:
                        dl[i][2][0] = 2
                    elif dl[i][2][0] == 2:
                        dl[i][2][0] = 1
                    elif dl[i][2][0] == 3:
                        dl[i][2][0] = 4
                    else:
                        dl[i][2][0] = 3
                # 흰색
                else:
                    if (tx, ty) in dp:
                        for j in range(len(dl)):
                            if dl[j][0] == tx and dl[j][1] == ty:
                                dl[j][2].append(reversed(dl[i][2]))
                                cnt = max(cnt, len(dl[j][2]))
                                delli.append(i)
                                break
                    else:
                        dp.remove((x, y))
                        dp.add((tx, ty))
                        dl[i][0] = tx
                        dl[i][1] = ty
            # 파란색
            else:
                if dl[i][2][0] == 1:
                    dl[i][2][0] = 2
                elif dl[i][2][0] == 2:
                    dl[i][2][0] = 1
                elif dl[i][2][0] == 3:
                    dl[i][2][0] = 4
                else:
                    dl[i][2][0] = 3

    # 드론제거
    # cnt 확인


    tim += 1
