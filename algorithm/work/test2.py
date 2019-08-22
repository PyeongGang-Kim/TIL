import time
import sys
sys.stdin = open('asdf.txt')


def fnf():
    global st
    X = len(nl)//2
    vl = [0 for _ in range(V+1)]
    for i in range(X):
        vl[nl[2*i+1]] += 1
    for i in range(1, V+1):
        if i not in st and not vl[i] and i in nl:
            st.append(i)


def delf():
    tmp = st.pop()
    result.append(tmp)
    tmpst = []
    for i in range(len(nl)//2):
        if nl[2*i] == tmp:
            tmpst.append(i)
    while tmpst:
        tmp2 = tmpst.pop()
        nl.pop(2*tmp2)
        nl.pop(2*tmp2)

T = 10
for t in range(1, T+1):
    V, E = map(int, input().split())
    nl = list(map(int, input().split()))
    st=[]
    result = []
    fnf()
    delf()
    while nl:
        while st:
            delf()
        fnf()
    print(result)