b=[input(),int(input())]
from datetime import datetime
c=datetime.today().year
c+=100-b[1]
print("{}(은)는 {}년에 100세가 될 것입니다.".format(b[0], c))