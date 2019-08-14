def insh(n):
    result.append(n)
    tmp = len(result) - 1
    sorth(tmp)



def sorth(idx):
    if result[idx] < result[idx//2]:
        tmp = idx//2
        result[idx], result[idx//2] = result[idx//2], result[idx]
        sorth(tmp)

def sumh():
    result2 = 0
    tmp = len(result) - 1
    while tmp:
        tmp //= 2
        result2 += result[tmp]
    return result2



T = int(input())
for t in range(1,T +1):
    N = int(input())
    result = [0]
    for n in map(int, input().split()):
        insh(n)
    print('#{} {}'.format(t, sumh()))
