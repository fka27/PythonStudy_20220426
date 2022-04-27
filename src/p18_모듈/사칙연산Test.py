import 사칙연산
print(사칙연산.sum(10, 20, 30, 40))


from 사칙연산 import sum, div
print(sum(10, 20, 30, 40))
print(div(100, 20, 2))


# #알리아스 -> 별명
import 사칙연산 as a
print(a.sum(10, 20, 30, 40))
print(a.div(100, 20, 2))
print(a.sub(100, 50))




print(a.getName())
print(a.__name__)

def sum(num, num2):
    return num + num2

name = input("사용 할 모듈을 입력하세요")

if a.__name__ == name:
    print(a.sum(10, 20))
elif __name__ == name:
    print(sum(50, 20))