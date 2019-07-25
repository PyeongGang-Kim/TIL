a=input().split("/")
print('protocol: {}'.format(a[0].split(":")[0]))
print('host: {}'.format(a[2]))
print('others: {}'.format(a[3]))