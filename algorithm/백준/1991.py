def pre(i = 0):
    r.append(chr(i+65))
    if nl[i][0] != '.':
        pre(ord(nl[i][0])-65)
    if nl[i][1] != '.':
        pre(ord(nl[i][1])-65)


def mid(i = 0):
    if nl[i][0] != '.':
        mid(ord(nl[i][0])-65)
    r.append(chr(i+65))
    if nl[i][1] != '.':
        mid(ord(nl[i][1])-65)


def pos(i = 0):
    if nl[i][0] != '.':
        pos(ord(nl[i][0])-65)
    if nl[i][1] != '.':
        pos(ord(nl[i][1])-65)
    r.append(chr(i+65))


N = int(input())
nl = [['.', '.'] for _ in range(N)]
for i in range(N):
    a, b, c = input().split()
    nl[ord(a)-65][0] = b
    nl[ord(a)-65][1] = c

r = []
pre()
print(''.join(r))

r = []
mid()
print(''.join(r))

r = []
pos()
print(''.join(r))