# 파일명을 변경하지 마시오.
# 아래에 클래스 Point와 Circle을 선언하시오.
class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y



class Circle:
    def __init__(self, p, r):
        self.x=p.x
        self.y=p.y
        self.r=r
    def get_area(self):
        return 3.14*self.r**2
    def get_perimeter(self):
        return 3.14*self.r*2
    def get_center(self):
        return (self.x, self.y)
    def __str__(self):
        return "Circle: {}, r:{}".format(self.get_center(),self.r)














# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    p1 = Point(0, 0)
    c1 = Circle(p1, 3)
    print(c1.get_area())
    print(c1.get_perimeter())
    print(c1.get_center())
    print(c1)
    p2 = Point(4, 5)
    c2 = Circle(p2, 1)
    print(c2.get_area())
    print(c2.get_perimeter())
    print(c2.get_center())
    print(c2)