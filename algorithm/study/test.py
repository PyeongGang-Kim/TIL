import math

a, b = map(int, input().split())
if a == b:
    if int(math.sqrt(a)) == math.sqrt(b):
        print(1)
    else:
        print(0)
else:
    print(b - a - (int(math.sqrt(b)) - math.ceil(math.sqrt(a))+1)+1)