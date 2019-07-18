class Shape:
    def __init__(self,leng):
        Shape.leng = leng

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        Square.length = length

    def area(self):
        return Square.length**2
a=Square(3)
print('정사각형의 면적: '+str(a.area()))