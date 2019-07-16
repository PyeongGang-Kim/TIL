a=[88,30,61,55,95]
for i,s in enumerate(a):
    if s>=60:
        print('{}번 학생은 {}점으로 합격입니다.'.format(i+1,s))
    else:
        print('{}번 학생은 {}점으로 불합격입니다.'.format(i+1,s))
