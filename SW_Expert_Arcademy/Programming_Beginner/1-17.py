b=input()
if b.isupper():
    print('{}(ASCII: {}) => {}(ASCII: {})'.format(b,ord(b),b.lower(),ord(b.lower())))
else:
    print('{}(ASCII: {}) => {}(ASCII: {})'.format(b,ord(b),b.upper(),ord(b.upper())))
