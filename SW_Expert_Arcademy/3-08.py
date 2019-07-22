T=int(input())
for t in range(T):
    input()
    results=[]
    resultNum, resultCnt=0,0
    ai=input()

    for i in range(10):
        results.append([i,0])

    for num in ai:
        results[int(num)][1] +=1

    for n, c in results:
        if resultCnt<=c:
            resultCnt=c
            resultNum=n

    print('#'+str(t+1),resultNum, resultCnt)
