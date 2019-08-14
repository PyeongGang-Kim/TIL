def nextp():
    global nd, B, p
    if goP(p):
        p = [p[0]+d[nd][0], p[1]+d[nd][1]]
        C[p[1]][p[0]] = B.pop(0)
    else:
        nd = (nd + 1)%4
        if goP(p):
            p = [p[0]+d[nd][0], p[1]+d[nd][1]]
            C[p[1]][p[0]] = B.pop(0)
        else:
            return
    return


def goP(p):
    global nd
    tmpp = [p[0] + d[nd][0], p[1] + d[nd][1]]
    if 0<=tmpp[0]<al and 0<=tmpp[1]<al:
        if C[tmpp[1]][tmpp[0]]:
            return False
        else:
            return True
    return False


A = [[9,20,2,18,11],[19,1,25,3,21],[8,24,10,17,7],[15,4,16,5,6],[12,13,22,23,14]]
al = len(A)
print(A)
B=[]
C = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
for a in A:
    B=B+a
for i in range(len(B)):
    for j in range(len(B)-1):
        if B[j]>B[j+1]:
            B[j], B[j+1] = B[j+1], B[j]
d = [[1,0], [0,1], [-1,0],[0,-1]]

nd = 0
p = [0, 0]
C[0][0] = B.pop(0)
while B:
    nextp()
for c in C:
    print(c)