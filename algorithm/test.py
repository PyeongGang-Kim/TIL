class asdf:
    def __init__(self):
        self.__a = 10

    def say(self):
        return self.__a

    def add(self):
        self.__a += 1

k = asdf()
print(k.say())
print(k.add())
print(k.say())
print(k.__a)