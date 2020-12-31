chkbit = 0b111111
D = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]

N, M, K = map(int, input().split())
pl = [list(map(int, input().split())) for _ in range(M)]


while K:
    K -= 1
    tpl = []
    temp_postion = dict()
    for planet in pl:
        y, x, m, s, d = planet
        tx, ty = (x + D[d][0] * s) % N, (y + D[d][1] * s) % N
        position = (tx << 6) + ty
        planet[0] = ty
        planet[1] = tx
        if temp_postion.get(position):
            temp_postion[position].append(planet)
        else:
            temp_postion[position] = [planet]
    for k, v in temp_postion.items():
        if len(v) == 1:
            tpl.append(v[0])
        else:
            x = k >> 6
            y = k & chkbit
            chk_value = v[0][4] & 1
            chk = False
            temp_mass = 0
            temp_speed = 0
            for planet in v:
                temp_mass += planet[2]
                temp_speed += planet[3]
                if planet[4] & 1 != chk_value:
                    chk = True
            temp_mass //= 5
            temp_speed //= len(v)
            if temp_mass:
                if not chk:
                    tpl.append([y, x, temp_mass, temp_speed, 0])
                    tpl.append([y, x, temp_mass, temp_speed, 2])
                    tpl.append([y, x, temp_mass, temp_speed, 4])
                    tpl.append([y, x, temp_mass, temp_speed, 6])
                else:
                    tpl.append([y, x, temp_mass, temp_speed, 1])
                    tpl.append([y, x, temp_mass, temp_speed, 3])
                    tpl.append([y, x, temp_mass, temp_speed, 5])
                    tpl.append([y, x, temp_mass, temp_speed, 7])
    pl = tpl
result = 0
for planet in pl:
    result += planet[2]

print(result)