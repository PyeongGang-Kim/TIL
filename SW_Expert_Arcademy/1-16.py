man1=input()
man2=input()

a=['가위','바위','보']
if a.index(man1)==a.index(man2):
    print('Result : Draw')
elif a[a.index(man1)-1]==a[a.index(man2)]:
    print('Result : Man1 Win!')
else:
    print('Result : Man2 Win!')