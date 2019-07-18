class Student:
    def __init__(self,name):
        Student.name=name
    def nnn(self):
        print("이름: "+ Student.name)
        
class GraduateStudent(Student):
    def __init__(self, name, major):
        GraduateStudent.name=name
        GraduateStudent.major=major
    def nnn(self):
        print("이름: "+ GraduateStudent.name + ", 전공: "+GraduateStudent.major)

stu_a=Student('홍길동')
stu_a.nnn()
stu_b=GraduateStudent('이순신', '컴퓨터')
stu_b.nnn()

