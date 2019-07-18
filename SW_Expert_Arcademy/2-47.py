class Circle:
    def __init__(self,R):
        Circle.R=R

    def area_circle(self):
        print('원의 면적: '+str(3.14*2*Circle.R))

a=Circle(2)
a.area_circle()

