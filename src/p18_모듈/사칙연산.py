def getName():
    return __name__
#덧셈
def sum(*args):     # *args -> 가변갯수
    result = 0            #result값은 0로 시작
    for num in args:      #args를 num에 대입하여
        result += num     #result에 num을 더하고
    return result         #result 값을 return해라
#뺄셈
def sub(*args):
    result = args[0] * 2
    for num in args:     #ex) sub(100, 20, 30)일 때 100-20-30 = 50이 되어야하는데
        result -= num    #   result값이 0으로 100을 빼면 -100이 되기 때문에
    return result        #   첫 값을 2배로 해두면 200-100-20-30=50이 된다
#곱셈
def mul(*args):
    result = 1      #result 값은 1로 시작(0에서 곱하면 0이 되기 때문)
    for num in args:
        result *= num
    return result
#나눗셈
def div(*args):
    result = args[0] * args[0]
    if 0 in args:    # 0이 args에 있다면
        return 0     # 0을 돌려주고
    for num in args: 
        result /= num
        return result

# sub(100, 20, 30)




#__name__ -> 모듈명
print(f'실행위치 {__name__}')

if __name__ == "__main__":
    print("현재 name이 main입니다.")


print("사칙연산 모듈")

print(mul(10, 2))