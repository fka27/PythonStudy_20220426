#클래스 이름 -> 첫글자가 대문자, 카멜표기법
#클래스 내부(속성, 기능)(변수, 함수(메소드))
#클래스 -> 틀
#틀에 의해서 생성 된 것 -> 객체(object)
#클래스 안에 있는 함수 = 메소드



class Student:      #class -> Student
    name = ""
    schoolName = ""
    studentYear = 0

    def __init__(self):
        print("생성자 호출됨")

    def showInfo(self):      #self -> 매개변수, s1과 s2의 주소(자기자신)
        print(f"학생이름: {self.name}")
        print(f"학교명: {self.schoolName}")
        print(f"학년: {self.studentYear}")
        print()
#Student라는 class는 showInfo라는 함수를 가진다.
s1=Student()     #s1으로 학생 한명(class => Student)을 생성해낸다.
s2=Student()

s1.name = "김가람"
s2.name = "김나람"

s1.schoolName = "부산대학교"
s2.schoolName = "부경대학교"

s1.studentYear = 1
s2.studentYear = 4

s1.showInfo()
s2.showInfo()

print(id(s1))
print(id(s2))
#변수 s1,s2의 주소출력