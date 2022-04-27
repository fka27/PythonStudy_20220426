number = 10

try:
    if number > 0:      #number가 0보다 크면
        pass            #pass
    else:               
        raise           #아니면 raise -> 예외발생을 시켜라(except로 이동)

except RuntimeError as e:     #오류가 발생 했을 시에는
    print(f"오류내용: {e}")   #"오류내용: RuntimeError" 를 출력
else:
    print("오류가 발생하지 않으면 실행")     #예외가 발생하지 않았을 때 출력
finally:
    print("무조건 실행")                    #예외와 상관없이 마지막에 출력되게 된다.



# number = -1

# try:
#     if number > 0:
#         pass
#     else:
#         raise FileNotFoundError
# except RuntimeError as e:
#     print(f"오류내용: {e}")
# else:
#     print("오류가 발생하지 않으면 실행")
# finally:
#     print("무조건 실행")
# print("프로그램 종료")



# number = -1

# try:
#     if number > 0:
#         pass
#     else:
#         raise FileNotFoundError
# except Exception as e:
#     import traceback
#     traceback.print_exc()
#     print(f"오류내용: {e}")
# else:
#     print("오류가 발생하지 않으면 실행")
# finally:
#     print("무조건 실행")
# print("프로그램 종료")



#예외 여러개 처리
# number = -1

# try:
#     if number > 0:
#         pass
#     elif number == -1:
#         list1 = [1,2,3,4,5]
#         list1.indea(6)
#     else:
#         raise FileNotFoundError
# except ValueError as e:
#     print(f"오류내용: {e}")
# except IndexError as e:
#     print(f"오류내용: {e}")
# except FileNotFoundError as e:
#     print(f"오류내용: {e}")
# except Exception as e:     #Exception -> 항상 마지막에
#     import traceback
#     traceback.print_exc()
#     print(f"오류내용: {e}")
# else:
#     print("오류가 발생하지 않으면 실행")
# finally:
#     print("무조건 실행")

# print("프로그램 종료")