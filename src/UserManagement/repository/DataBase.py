import json

class DataBase:
    data = {
        "user_mst": list()
    }

    def __init__(self):
        try:
            with open("./src/UserManagement/userdata.json", "r", encoding="utf8") as f:
                self.data = json.load(f)     #파일을 읽어들인다
        except FileNotFoundError:
            with open("./src/UserManagement/userdata.json", "w", encoding="utf8") as f:
                json.dump(self.data, f, indent=4)     #파일이 없으면 생성한다
            with open("./src/UserManagement/userdata.json", "r", encoding="utf8") as f:
                self.data = json.load(f)     #그러고 다시 읽어들인다


    def getData(self):
        return self.data

    def save(self):     #save -> 해당 딕셔너리 안에 들어있는 값은 덮어쓴다.
        print(self.data)
        with open("./src/UserManagement/userdata.json", "w", encoding="utf8") as f:
            json.dump(self.data,f, indent=4, ensure_ascii=False)
