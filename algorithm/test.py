T= int(input())

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def go(y,x,length, keep_chance, before_height):
    global answer
    c_chance = keep_chance
    for i in range(0, len(dy)):
        current_y = y + dy[i]
        current_x = x + dx[i]

        if current_y < 0 or current_y >= N or current_x < 0 or current_x >= N:
            continue

        if [current_y, current_x] in visit:
            continue

        if before_height <= map_list[current_y][current_x]:  # can't go because of height
            if c_chance==1 and K > map_list[current_y][current_x] - before_height:
                current_height = before_height-1
                c_chance=0
            else:
                continue
        else:
            current_height = map_list[current_y][current_x]

        current_length = length + 1
        if answer < current_length:
            answer=current_length
        visit.append([current_y,current_x])
        go(current_y, current_x, current_length, c_chance, current_height)
        visit.pop(-1)


for t in range(1,T+1):
    global N, K, map_list, stack, answer

    answer=0

    N,K = map(int,input().split())

    map_list=[]

    for y in range(0,N):
        map_list.append(list(map(int,input().split())))

    # find highest height
    start_height = 0
    for y in range(0,N):
        start_height = max(start_height, max(map_list[y]))


    temp_list=list(map(list,map_list))

    for y in range(0,N):
        for x in range(0,N):

            if map_list[y][x]==start_height:
                visit = []
                length = 1
                visit.append([y,x])
                go(y,x,length,1,map_list[y][x])
                visit.pop(-1)

    print("#%d %d"%(t,answer))