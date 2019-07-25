R=['가위', '바위', '보']
man1=input()
man2=input()
man1_a=input()
man2_a=input()
for i, k in enumerate(R):
    if man1_a==k:
        man1_b=i
    if man2_a==k:
        man2_b=i
if R[man1_b]==R[man2_b]:
    print('비겼습니다.')

elif R[man1_b]==R[man2_b-1]:
    print('{}가 이겼습니다!'.format(R[man2_b]))

else:
    print('{}가 이겼습니다!'.format(R[man1_b]))