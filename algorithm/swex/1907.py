def mel(x, y, idx):
    for dx, dy in D:
        tx, ty = x + dx, y + dy
        if 0 <= tx < W and 0 <= ty < H and ml[ty][tx] and ml2[ty][tx]:
            ml2[ty][tx] -= 1
            if not ml2[ty][tx]:
                tmps[idx].append([tx, ty])


D = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
tmps = [[], []]
T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    ml = [[int(num) if num != '.' else 0 for num in list(input())] for _ in range(H)]
    ml2 = [[ml[y][x] for x in range(W)] for y in range(H)]
    for y in range(H):
        for x in range(W):
            if not ml[y][x]:
                mel(x, y, 0)

    idx1 = 0
    idx2 = 1
    cnt = 0
    while tmps[idx1]:
        cnt += 1
        tmp = []
        for item in tmps[idx1]:
            if ml[item[1]][item[0]]:
                ml[y][x] = 0
                tmp.append(item)
        tmps[idx1] = []
        while tmp:
            x, y = tmp.pop()
            mel(x, y, idx2)
        if not tmps[idx2]:
            break
        idx1 ^= 1
        idx2 ^= 1
    print('#{} {}'.format(tc, cnt))

