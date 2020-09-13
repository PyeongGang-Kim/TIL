def solution(maze):
    D = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    N = len(maze)
    cx, cy = 0, 0
    cnt = 0
    # 처음에 오른쪽 보면서 시작
    d = 1

    # 손이 벽을 보고있는지 확인한다.
    tx, ty = cx + D[d - 1][0], cy + D[d - 1][1]
    # 손이 벽을 향하지 않으면 회전
    while 0 <= tx < N and 0 <= ty < N and not maze[ty][tx]:
        d = (d + 1) % 4

    while not (cx == N - 1 and cy == N - 1):
        # 전진 시도
        tx, ty = cx + D[d][0], cy + D[d][1]
        # 전진할 수 있으면 cnt+1
        if 0 <= tx < N and 0 <= ty < N and not maze[ty][tx]:
            cnt += 1
            cx, cy = tx, ty
            # 벽이 있는지 확인 후 없으면 회전 1회
            tx, ty = cx + D[d - 1][0], cy + D[d - 1][1]
            if 0 <= tx < N and 0 <= ty < N and not maze[ty][tx]:
                d = (d - 1) % 4

        # 전진하지 못하면 회전
        else:
            d = (d + 1) % 4

    answer = cnt
    return answer
print(solution([[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]]))