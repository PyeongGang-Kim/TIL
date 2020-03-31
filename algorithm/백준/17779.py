N = int(input())
nl = [list(map(int, input().split())) for _ in range(N)]

sn = 0
result = 40000
for j in range(N):
    for i in range(N):
        sn += nl[j][i]
for j in range(N-2):
    for i in range(1, N-1):
        for l in range(i-1, -1, -1):
            for r in range(i+1, N):
                ly = j+i-l
                ry = j+r-i
                ex = r-i+l
                ey = j+r-l
                if ey >= N:
                    break
                # print(i, j, l, ly, r, ry, ex, ey)
                S = [0, 0, 0, 0, 0]
                for h1 in range(j):
                    for w1 in range(i+1):
                        S[0] += nl[h1][w1]
                    for w2 in range(i+1, N):
                        S[1] += nl[h1][w2]
                for h1 in range(j, ly):
                    for w1 in range(i-(h1-j)):
                        S[0] += nl[h1][w1]
                for h2 in range(j, ry+1):
                    for w2 in range(i+1+(h2-j), N):
                        S[1] += nl[h2][w2]
                tmpmax = max(S[0], S[1])
                tmpmin = min(S[0], S[1])
                if tmpmax-tmpmin >= result:
                    continue
                for h3 in range(ey+1, N):
                    for w3 in range(ex):
                        S[2] += nl[h3][w3]
                    for w4 in range(ex, N):
                        S[3] += nl[h3][w4]
                for h3 in range(ly, ey+1):
                    for w3 in range(l+(h3-ly)):
                        S[2] += nl[h3][w3]
                tmpmax = max(tmpmax, S[2])
                tmpmin = min(tmpmin, S[2])
                if tmpmax-tmpmin >= result:
                    continue
                for h4 in range(ry+1, ey+1):
                    for w4 in range(r-(h4-ry-1), N):
                        S[3] += nl[h4][w4]
                S[4] = sn-sum(S)
                tmpmax = max(tmpmax, S[3], S[4])
                tmpmin = min(tmpmin, S[3], S[4])
                result = min(result, tmpmax-tmpmin)
print(result)