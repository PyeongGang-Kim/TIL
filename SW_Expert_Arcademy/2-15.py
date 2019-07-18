import math
a=list(map(float,input().split(", ")))
print(', '.join([str(round(i*math.pi*2,2)) for i in a]))