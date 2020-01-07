u = 100
ul = [i&-i for i in range(1000)]
ulb = [[(i), bin(-i)] for i in range(1000)]
while u:
    u&=u-1