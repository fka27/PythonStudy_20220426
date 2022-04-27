# money = True


# if money:
#     print("저축을 해라")
# else:
#     print("돈을 벌어라")



# point = 350


# if point > 999 :
#     print("다이아 회원") #1000 이상
# elif point > 599 :
#     print("골드 회원") #600 이상
# elif point > 299 :
#     print("실버 회원") #300 이상
# elif point > 99 :
#     print("브론즈 회원") #100 이상
# else :
#     print("신규회원") #0 이상


# point = 800

# if point > 999 :
#     print("다이아 회원")
# elif point > 599 :
#     print("골드 회원")
# elif point > 299 :
#     print("실버 회원")
# elif point > 99 :
#     print("브론즈 회원")
# else :
#     print("신규회원")



# point = 1000

# result = ("다이아회원" if point > 999 else "골드회원") if point > 599 else ("실버회원" if point > 299 else "브론즈회원")
# print(result)



#input -> 출력값에 타이핑을 할 수 있는 함수
# food = input()
# print(food)

# food = input("생각나는 음식을 적어주세요: ") #출력값 옆에 타이핑
# print(f"출력 확인: {food}")

# print("생각나는 음식을 적어주세요: ") #출력값 밑에 타이핑
# food = input() 
# print(f"출력 확인: {food}")



#숫자를 입력 받아서 산술연산자 사용

# num1 = int(input("첫번째 수를 입력해주세요: "))
# num2 = int(input("두번째 수를 입력해주세요: "))
#str형태로 출력되기 때문에 int함수 사용
#텍스트
# print(f"덧셈 : {num1 + num2}")
# print(f"뺄셈 : {num1 - num2}")
# print(f"곱셈 : {num1 * num2}")
# print(f"나눗셈 : {num1 / num2}")
# print(f"제곱 : {num1 ** num2}")
# print(f"몫 : {num1 // num2}")
# print(f"나머지 : {num1 % num2}")




# import random     #랜덤을 불러온다.

# menu = "돈가스", "피자", "치킨", "국수", "소고기", "회"
# print(random.choice(menu))
# 위의 메뉴들 중에서 랜덤으로 한가지가 선택된다.




# sys - 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어 할 수 있게 해주는 모듈
#     - .argv: 명령 행에서 인수 전달
#     - .exit: 강제 스크립트 종료
#     - .path: 파일을 불러올 수 있는 함수
# pickle - 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러 올 수 있게 하는 모듈
# os - 환경변수, 디렉터리, 파일 등의 os자원을 제어 해주는 모듈
#    - .environ: 현재 시스템의 환경 변수 값을 보여줌
#    - .chdir: 현재 디렉터리 위치 변경
#    - .getcwd: 현재 디렉터리 위치를 돌려줌
#    - .system: 명령어 호출
#    - .popen: 명령어를 실행한 결괏값을 읽기 모드 형태의 파일 객체로 돌려줌
# shutil - 파일을 복사해주는 모듈
# glob - 디렉터리 안의 파일들을 리스트로 만들어주는 모듈
# tempfile - 파일을 임시로 만들어서 사용하는 모듈
# time - 시간 관련 모듈
#      - .time: 현재시간을 초 단위까지 알려주는 함수
# calender - 달력 모듈
# random - 난수 모듈(규칙이 없는 수(랜덤))
# webbrowser - 웹 브라우저를 자동으로 실행하는 모듈




# dir - 객체가 자체적으로 가지고 있는 변수나 함수를 보여주는 함수
# filter - 무엇인가를 걸러내어주는 함수
# id - 객체를 입력받아 객체의 고유 주소를 돌려주는 함수
# input - 사용자가 직접 입력할 수 있는 함수
# int - 문자열이나 실수 형태의 숫자를 정수 형태로 바꾸어 주는 함수
# isinstance - (object, class) 입력받은 object가 class의 object인지 판단해주는 함수(참, 거짓)
# len - 입력값의 길이를 알려주는 함수
# list - 반복가능한 자료형을 입력 받아서 리스트로 돌려주는 함수
# max - 반복 가능한 자료형을 입력 받아서 최댓값으로 돌려주는 함수
# min - 반복 가능한 자료형을 입력 받아서 최솟값으로 돌려주는 함수
# open - 파일을 "w" 쓰기모드/ "r" 읽기모드로 돌려주는 함수
# range - 해당 범위 내에서 차례대로 출력, for문과 자주 사용하는 함수
# str - 문자열 형태로 돌려주는 함수
# sum - 입력받은 리스트나 튜플의 모든 요소의 합을 돌려주는 함수
# tuple - 튜플 형태로 돌려주는 함수
# type - 어떤 자료형인지 알려주는 함수
# zip - 동일한 갯수로 이루어진 자료형을 각 각 순서를 함께 묶어주는 함수
