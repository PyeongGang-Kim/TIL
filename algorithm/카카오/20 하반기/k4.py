nl = [[0]*300 for _ in range(300)]

def solution(n, s, a, b, fares):
    # 플로이드 써서 이동거리 구하기 n^3
    for fare in fares:
        fare[0] -= 1
        fare[1] -= 1
        nl[fare[0]][fare[1]] = fare[2]
        nl[fare[1]][fare[0]] = fare[2]
    # for j in range(n):
    #     print(nl[j][:n])
    # print("...")
    for k in range(n):
        for j in range(n):
            for i in range(n):
                if i == j:
                    break
                if nl[j][k] and nl[k][i]:
                    if nl[j][i]:
                        nl[j][i] = min(nl[j][i], nl[j][k] + nl[k][i])
                        nl[i][j] = nl[j][i]
                    else:
                        nl[j][i] = nl[j][k] + nl[k][i]
                        nl[i][j] = nl[j][i]
    for j in range(n):
        print(nl[j][:n])


    # 시작점 ~ 중간점 + 중간점 ~ A, 중간점 ~ B 의 최소값 구하기
    answer = 0xfffffff
    s -= 1
    a -= 1
    b -= 1
    for i in range(n):
        if nl[s][i] + nl[i][a] + nl[i][b] < answer:
            answer = nl[s][i] + nl[i][a] + nl[i][b]
    return answer

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))