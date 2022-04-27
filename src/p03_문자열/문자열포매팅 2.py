str1 = "첫번째 수 {} 두번째 수 {} 두수의 합{}". format(15, 80, 15+80)
print(str1)

num1 = 10
num2 = 20
num3 = num1 + num2
str2 = "첫번째 수 {0} 두번째 수 {1} 두수의 합{2}". format(num1, num2, num3)
print(str2)
str3 = "첫번째 수 {num1} 두번째 수 {num2} 두수의 합{num3}". format(num1 = 55, num2 = 140, num3 = 55 + 140)
print(str3)

str5 = "문자열 포매팅 왼쪽 정렬ㅣ{:<10}ㅣ". format("3월")
print(str5)
str6 = "문자열 포매팅 오른쪽 정렬ㅣ{:>10}ㅣ". format("3월")
print(str6)
str7 = "문자열 포매팅 가운데 정렬ㅣ{:^10}ㅣ". format("3월")
print(str7)
str8 = "문자열 포매팅 가운데 정렬 후 공백 채우기ㅣ{:!^10}ㅣ". format("3월")
print(str8)

str8 = "문자열 포매팅 왼쪽 정렬 후 공백채우기ㅣ{0:ㅏ<10.4f}ㅣ". format(3.323545)
print(str8)

str9 = "문자열 포매팅 {0} {{가람}}". format("김")
print(str9)
