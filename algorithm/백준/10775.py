import sys
input = sys.stdin.readline

def unionfind(i):
    if cl[i] != -1:
        cl[i] = unionfind(cl[i])
        return cl[i]
    else:
        return i


G = int(input())
P = int(input())
cl = [-1 for _ in range(G+1)]
num = 0
while num < P:
    g = int(input())
    if cl[g] != -1:
        tmp = unionfind(g)
        if tmp:
            cl[tmp] = unionfind(tmp-1)
            cl[g] = cl[tmp]
        else:
            break
    else:
        cl[g] = unionfind(g-1)
    num += 1
print(num)