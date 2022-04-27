n = int(input("별의 개수: "))
i = 0

while i < n:
    i += 1
    print("*" * i) #왼쪽정렬


n = int(input("별의 개수: "))
i = 0

while i < n:
    print("*" * (n-i))
    i += 1 #왼쪽정력 역배열




n = int(input("별의 개수: "))
i = 0

while i < n:
    i += 1
    print("{:>5}".format("*" * i)) #오른쪽 정렬(변수 지정 불가)


n = int(input("별의 개수: "))
i = 0

while i < n:
    i += 1
    print(" " * (n - i), end= '')
    print("*" * i) #오른쪽 정렬


n = int(input("별의 개수: "))
i = 0

while i < n:
    i += 1
    print(" " * (n - i) + ("*" * i)) #오른쪽 정렬




n = int(input("별의 개수: "))
i = 0

while i < n:
    print(" " * i + ("*" * (n - i)))
    i += 1 #오른쪽 정렬 역배열


