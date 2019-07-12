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



#3. 도시별 최근 3일 온도입니다.
city={
    '서울': [-6, -10, 5],
    '대전': [-4, -5, 2],
    '광주': [0,-2,-10],
    '부산': [2,-2,9]
}


#3-1. 도시별 최근 3일의 온도 평균은?

for i in city:
    cnt=0
    sum=0
    for k in city[i]:
        sum+=k
        cnt+=1
    print(sum/cnt)


    
#3-2. 도시 중 최근 3일 중에 가장 추웠던, 가장 더웠던 곳은?
sum=0
cnt=0
hest=[-100,0]
lest=[100,0]
for i in city:
    for k in city[i]:
        if hest[0]<k:
            hest[1]=i
            hest[0]=k
        if lest[0]>k:
            lest[1]=i
            lest[0]=k
print(hest[1],lest[1])



#3-3. 서울은 영상 2도였던 적이 있나요?
print(2 in city['서울'])
