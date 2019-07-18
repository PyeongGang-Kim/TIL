class Person:
    def getGender(self):
        return "Unknown"


class Male(Person):
    def getGender(self):
        return "Male"


class Female(Person):
    def getGender(self):
        return "Female"

a=Male()
b=Female()
print(a.getGender())
print(b.getGender())