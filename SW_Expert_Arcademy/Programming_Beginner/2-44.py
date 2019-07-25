class stu:
    def 입력(self,국어, 영어, 수학):
        stu.국어=int(국어)
        stu.영어=int(영어)
        stu.수학=int(수학)
    def 합계(self):
        result=stu.국어+stu.영어+stu.수학
        return result
b=list(map(int,input().split(", ")))
a=stu()
a.입력(*b)
print("국어, 영어, 수학의 총점: %d" %a.합계())
