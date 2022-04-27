strName = "김준일, 김기덕, 송지한, 전주홍"

print(strName.find("김기덕"))

print(strName.find("노신비"))
try:
    print(strName.index("노신비"))    #index는 없는 값 출력 할 때 오류 -> try except사용 필수
except:
    print("예외가 발생하였습니다.")

print("프로그램 정상종료")







# fruit = "사과, 바나나, 파인애플, 복숭아, 딸기"

# print(fruit.find("파인애플")) 

# print(fruit.find("블루베리"))

# try:
#     print(fruit.index("블루베리")) 
# except:
#     print("예외가 발생하였습니다.")

# print("프로그램 정상종료")

#find는 값이 없어도 오류가 나지 않음
#index는 값이 없으면 오류발생 -> try, except 사용으로 오류가 나는지 확인 가능