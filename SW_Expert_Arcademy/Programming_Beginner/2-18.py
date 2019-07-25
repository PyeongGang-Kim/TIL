c=list(map(int,input().split(", ")))
print(", ".join([str(i) for i in c if i%2!=0]))
