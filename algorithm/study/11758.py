'''
p2p1 벡터와 p2p3 벡터의 외적을 구하면 되는 문제.
외적이 양의 값일 경우 반시계, 음의 값일 경우 시계
0일 경우 평행하다.
'''
p1x, p1y = map(int, input().split())
p2x, p2y = map(int, input().split())
p3x, p3y = map(int, input().split())
tmp =  (p1x-p2x) * (p3y-p2y) - (p3x - p2x) * (p1y - p2y)
if tmp < 0:
    print(1)
elif tmp > 0:
    print(-1)
else:
    print(0)