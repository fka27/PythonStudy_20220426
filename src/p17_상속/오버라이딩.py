class 아부지:
    carModel = ""
    carColor = ""

    def showCarInfo(self):
        self.carColor = "화이트"
        print("[차량정보]")
        print(f"차량 모델: {self.carModel}")
        print(f"차량 색상: {self.carColor}")
        
class 자식(아부지):
    def showCarInfo(self):
        self.carColor = "블랙"
        print("[차량정보]")
        print(f"차량 모델: {self.carModel}")
        print(f"차량 색상: {self.carColor}")

가람 = 자식()
가람.carModel = "쏘나타"
가람.showCarInfo()





# class 부모:
#     house = ""
#     interior = ""

#     def showCarInfo(self):
#         self.interior = "북유럽컨셉"
#         print("[집 정보]")
#         print(f"주택형태: {self.house}")
#         print(f"인테리어: {self.interior}")
        
# class 자식(부모):
#     def showCarInfo(self):
#         self.interior = "심플컨셉"
#         print("[집 정보]")
#         print(f"주택형태: {self.house}")
#         print(f"인테리어: {self.interior}")

# 가람 = 자식()
# 가람.house = "단독주택"
# 가람.showCarInfo()