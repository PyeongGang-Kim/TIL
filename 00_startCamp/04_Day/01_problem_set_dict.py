"""
Python dictionary 문제
"""
#1. 평균을 구하세요
score={
    '수학':80,
    '국어':90,
    '음악':100
}
a=score.values()
print(a)
print(sum(a)/len(a))

#2. 반 평균을 구하세요. -> 전체 평균
scores={
    'a': {
        '수학':80,
        '국어':90,
        '음악':100
    },
    'b': {
        '수학':80,
        '국어':90,
        '음악':100
    }
}


sum=0
cnt=0
for i in scores:
    a=scores[i].values()
    for k in a:
        sum+=k
        cnt+=1

print(sum/cnt)
