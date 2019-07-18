'''
방법 1.

a="ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
print(sum(list(map(lambda x: (x=="A")*4,a)))+sum(list(map(lambda x: (x=="B")*3,a)))+sum(list(map(lambda x: (x=="C")*2,a)))+sum(list(map(lambda x: (x=="D")*1,a))))

'''


'''
방법 2.

a="ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
A=[4 for s in a if s=='A']
B=[3 for s in a if s=='B']
C=[2 for s in a if s=='C']
D=[1 for s in a if s=='D']
result=sum(A+B+C+D)
print(result)

'''