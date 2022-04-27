
for i in range(1, 11):
    print("*"* i)


# for i in range(10,0,-1):
#     print("*" * i)
for i in range(10):
    print("*" * (10-i))





for i in range(0,11):
    print((" " * (11-1-i)) + ("*" * i))


# for i in range(10,0,-1):
#     print((" " * (10-i)) + ("*" * i))
for i in range(1,11):
    print((" " * (i-1)) + ("*" * (11-i)))





for i in range(5):
    for k in range(5,i,-1):
        print(" ", end='')
    for k in range((i+1)*2-1):
        print("*",end='')
    print()











list1 = range(2,10)


for i in range(1,11):
    print("*" * i)

for i in range(10,0,-1):
    print("*" * i)

for i in range(0,11):
    print((" " * (11-1-i)) + ("*" * i))

for i in range(10,0,-1):
    print((" " * (10-i)) + ("*" * i))

for i in range(0,5):
    print(" " * (5 - i - 1) + ("*" * ((i * 2) + 1)))

for i in range(5,0,-1):
    print((" " * (5 - i)) + ("*" * (( i * 2) - 1)))
    