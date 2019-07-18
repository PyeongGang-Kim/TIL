student = [(90, 80), (85, 75), (90, 100)]
for i in range(0,len(student)):
    print("{}번 학생의 총점은 {}점이고, 평균은 {}입니다.".format(i+1,student[i][0]+student[i][1],(student[i][0]+student[i][1])/2))