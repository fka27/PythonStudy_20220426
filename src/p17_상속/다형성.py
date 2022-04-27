class Factory:
    def start(self):     #상속을 받아서 start라는 메소드를 쓴다.(의미상 정의)
        pass

class ComputerFactory(Factory):
    def start(self):
        print("컴퓨터 생산 라인을 가동합니다.")

class AirConditionerFactory(Factory):
    def start(self):
        print("에어컨 생산 라인을 가동합니다.")


factoryList = list()

cf = ComputerFactory()
af = AirConditionerFactory()

factoryList.append(cf)
factoryList.append(af)

for factory in factoryList:
    factory.start()