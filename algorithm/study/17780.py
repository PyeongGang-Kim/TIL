D = [[], [1, 0], [-1, 0], [0, -1], [0, 1]]
DX = {1: 2, 2: 1, 3: 4, 4: 3}
N, K = map(int, input().split())
nl = [list(map(int, input().split())) for _ in range(N)]
dl = []
dp = set()
for k in range(K):
    y, x, d = map(int, input().split())
    dl.append([x-1, y-1, [d]])
    dp.add((x-1, y-1))
tim = 0
cnt = 1
if len(dl) < 4:
    tim = 1001

while tim < 1001:
    tim += 1
    # 드론들 순번대로 이동한다
    delli = []
    for i in range(len(dl)):
        x, y = dl[i][0], dl[i][1]
        d = dl[i][2][0]
        tx, ty = x + D[d][0], y + D[d][1]

        if 0 <= tx < N and 0 <= ty < N:
            # 빨간색
            if nl[ty][tx] == 1:
                # 빨간색 드론 밟음
                if (tx, ty) in dp:
                    for j in range(len(dl)):
                        if dl[j][0] == tx and dl[j][1] == ty:
                            dl[i][2].reverse()
                            dl[j][2] = dl[j][2] + dl[i][2]
                            cnt = max(cnt, len(dl[j][2]))
                            dp.remove((x, y))
                            delli.append(i)
                            break
                # 빨간색 드론 안밟음
                else:
                    dp.remove((x, y))
                    dp.add((tx, ty))
                    dl[i][0] = tx
                    dl[i][1] = ty
                    dl[i][2].reverse()
            # 파란색
            elif nl[ty][tx] == 2:
                dl[i][2][0] = DX[dl[i][2][0]]
                tx2, ty2 = x - D[d][0], y - D[d][1]
                if 0 <= tx2 < N and 0 <= ty2 < N:
                    # 파란색 - 빨간색
                    if nl[ty2][tx2] == 1:
                        # 파란색 빨간색 드론 밟음
                        if (tx2, ty2) in dp:
                            for j in range(len(dl)):
                                if dl[j][0] == tx2 and dl[j][1] == ty2:
                                    dl[i][2].reverse()
                                    dl[j][2] = dl[j][2] + dl[i][2]
                                    cnt = max(cnt, len(dl[j][2]))
                                    dp.remove((x, y))
                                    delli.append(i)
                                    break
                        # 파란색 빨간색 드론 안밟음
                        else:
                            dp.remove((x, y))
                            dp.add((tx2, ty2))
                            dl[i][2].reverse()
                            dl[i][0] = tx2
                            dl[i][1] = ty2
                    # 파란색 - 파란색
                    elif nl[ty2][tx2] == 2:
                        dl[i][2][0] = DX[dl[i][2][0]]
                    # 파란색 - 흰색
                    else:
                        # 파란색 흰색 드론 밟음
                        if (tx2, ty2) in dp:
                            for j in range(len(dl)):
                                if dl[j][0] == tx2 and dl[j][1] == ty2:
                                    dl[i][2].reverse()
                                    dl[j][2] = dl[j][2] + dl[i][2]
                                    cnt = max(cnt, len(dl[j][2]))
                                    dp.remove((x, y))
                                    delli.append(i)
                                    break
                        # 파란색 흰색 드론 안밟음
                        else:
                            dp.remove((x, y))
                            dp.add((tx2, ty2))
                            dl[i][0] = tx2
                            dl[i][1] = ty2
                # 파란색 - 파란색
                else:
                    dl[i][2][0] = DX[dl[i][2][0]]
            # 흰색
            else:
                # 흰색 드론 밟음
                if (tx, ty) in dp:
                    for j in range(len(dl)):
                        if dl[j][0] == tx and dl[j][1] == ty:
                            dl[i][2].reverse()
                            dl[j][2] = dl[j][2] + dl[i][2]
                            dp.remove((x, y))
                            cnt = max(cnt, len(dl[j][2]))
                            delli.append(i)
                            break
                # 흰색 드론 안밟음
                else:
                    dp.remove((x, y))
                    dp.add((tx, ty))
                    dl[i][0] = tx
                    dl[i][1] = ty
        # 파란색
        else:
            dl[i][2][0] = DX[dl[i][2][0]]
            tx2, ty2 = x - D[d][0], y - D[d][1]
            if 0 <= tx2 < N and 0 <= ty2 < N:
                # 파란색 - 빨간색
                if nl[ty2][tx2] == 1:
                    # 파란색 빨간색 드론 밟음
                    if (tx2, ty2) in dp:
                        for j in range(len(dl)):
                            if dl[j][0] == tx2 and dl[j][1] == ty2:
                                dl[i][2].reverse()
                                dl[j][2] = dl[j][2] + dl[i][2]
                                dp.remove((x, y))
                                delli.append(i)
                                break
                    # 파란색 빨간색 드론 안밟음
                    else:
                        dp.remove((x, y))
                        dp.add((tx2, ty2))
                        dl[i][2].reverse()
                        dl[i][0] = tx2
                        dl[i][1] = ty2
                # 파란색 - 파란색
                elif nl[ty2][tx2] == 2:
                    dl[i][2][0] = DX[dl[i][2][0]]
                # 파란색 - 흰색
                else:
                    # 파란색 흰색 드론 밟음
                    if (tx2, ty2) in dp:
                        for j in range(len(dl)):
                            if dl[j][0] == tx2 and dl[j][1] == ty2:
                                dl[i][2].reverse()
                                dl[j][2] = dl[j][2] + dl[i][2]
                                cnt = max(cnt, len(dl[j][2]))
                                dp.remove((x, y))
                                delli.append(i)
                                break
                    # 파란색 흰색 드론 안밟음
                    else:
                        dp.remove((x, y))
                        dp.add((tx2, ty2))
                        dl[i][0] = tx2
                        dl[i][1] = ty2
            # 파란색 - 파란색
            else:
                dl[i][2][0] = DX[dl[i][2][0]]

    # 드론제거
    delli.reverse()
    for idx in delli:
        dl.pop(idx)

    # cnt 확인
    if cnt >= 4:
        break
if tim == 1001:
    print(-1)
else:
    print(tim)

