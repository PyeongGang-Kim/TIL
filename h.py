def sqrt_test(n):
    s=0
    e=n
    is_sol=(s+e)/2
    while abs(is_sol**2 - n)>0.00000000001:
        s,e=find_sol_bi(n,s,e)
        is_sol=(s+e)/2
    return is_sol

def find_sol_bi(n,s,e):
    nn=(s+e)/2
    if nn**2>n:
        return s, nn
    else:
        return nn, e

print(sqrt_test(2))