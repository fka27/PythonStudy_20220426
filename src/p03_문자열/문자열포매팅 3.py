#f문자열 포매팅
#python 3.6버전 이상부터 지원.

name = "홍길동"
name1 = "홍길동1"
address = "부산광역시 해운대구"

str1 = f"이름: {name}, {name1}"
str2 = f"주소: {address}"

print(str1)
print(str2)

str1 = f"이름: {name:?^10} {{name}}"
str2 = f"주소: {address:>10}"

print(str1)
print(str2)
