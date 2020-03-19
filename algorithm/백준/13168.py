import sys
input = sys.stdin.readline
inf = 0xfffffffffff

t_type = {
    "Subway": 0,
    "Bus": 0,
    "Taxi": 0,
    "Airplane": 0,
    "KTX": 0,
    "S-Train": 2,
    "V-Train": 2,
    "ITX-Saemaeul": 1,
    "ITX-Cheongchun": 1,
    "Mugunghwa": 1,
}
N, R = map(int, input().split())
cities = {city: i for i, city in enumerate(input().split())}
M = int(input())
nl = [cities[city] for city in input().split()]
K = int(input())
ml = [[[inf for _ in range(N)] for _ in range(N)] for _ in range(2)]
for i in range(N):
    ml[0][i][i] = 0
    ml[1][i][i] = 0
while K:
    K -= 1
    temp_type, S, E, Cost = input().split()
    city_s, city_e, cost = cities[S], cities[E], int(Cost)
    cost2 = cost << 1
    tmp = t_type[temp_type]
    if tmp:
        if tmp == 1:
            ml[0][city_s][city_e] = min(ml[0][city_s][city_e], cost2)
            ml[0][city_e][city_s] = ml[0][city_s][city_e]
            ml[1][city_s][city_e] = 0
            ml[1][city_e][city_s] = 0
        else:
            ml[0][city_s][city_e] = min(ml[0][city_s][city_e], cost2)
            ml[0][city_e][city_s] = ml[0][city_s][city_e]
            ml[1][city_s][city_e] = min(ml[1][city_s][city_e], cost)
            ml[1][city_e][city_s] = ml[1][city_s][city_e]
    else:
        ml[0][city_s][city_e] = min(ml[0][city_s][city_e], cost2)
        ml[0][city_e][city_s] = ml[0][city_s][city_e]
        ml[1][city_s][city_e] = min(ml[1][city_s][city_e], cost2)
        ml[1][city_e][city_s] = ml[1][city_s][city_e]

for l in range(2):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                ml[l][i][j] = min(ml[l][i][j], ml[l][i][k] + ml[l][k][j])
r = [0, 0]
for l in range(2):
    for i in range(len(nl)-1):
        r[l] += ml[l][nl[i]][nl[i+1]]

if r[1] + (R<<1) >= r[0]:
    print("No")
else:
    print("Yes")