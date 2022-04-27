import time     #time을 불러온다

print("데이터 저장중...")
for i in range(100):
    print(str(i+1),"/", str(100))
    time.sleep(0.3)
#-> 0.3초씩 끊어서 100개의 데이터를 저장한다.