
class Student:      #class -> Student
    name = ""
    schoolName = ""
    studentYear = 0

    def __init__(self):           #(파이썬 지정) 기본 생성자 => __init__
        print("생성자 호출됨")     #(파이썬 지정) 클래스 첫번째 매개변수 => self


Student()
s1 = Student()
# __init__ -> 객체를 생성 할 시점에 자동으로 출력을 해줌
# 출력을 하고 싶지 않을 때 print 대신 pass를 입력하면 출력이 되지 않음
