name = "김준일"
phone = "010-9988-1916"
email = "skjil1218@kakao.com"

print(name)
print(phone)
print(email)

name = "홍길동"
number = "881120-1068234"

#인덱싱
year = 0;
month = 0;
day = 0;
print("year변수의 타입: ", type(year))

year = "19" + number[0] + number[1]
print("year변수의 타입: ", type(year))
print(year)

month = number[2] + number[3]
day = number[4] + number[5]

print(year + month + day)
print(number[7:])


