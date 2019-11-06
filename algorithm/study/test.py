a, b = input().strip().split()
tmp = set(a).intersection(set(b))
for i in range(len(a)):
    if a[i] in tmp:
        ai = i
        break

for i in range(len(b)):
    if b[i] == a[ai]:
        bi = i
        break
nl = [['.' for _ in range(len(a))] for _ in range(len(b))]

for j in range(len(b)):
    nl[j][ai] = b[j]

nl[bi] = list(a)
for j in range(len(b)):
    nl[j] = ''.join(nl[j])
print('\n'.join(nl))