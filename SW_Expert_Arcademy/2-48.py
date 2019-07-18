class Rect:
    def __init__(self,h,w):
        Rect.h=h
        Rect.w=w
    def cal_A(self):
        print('사각형의 면적: '+str(Rect.h*Rect.w))

사각형=Rect(4,5)
사각형.cal_A()