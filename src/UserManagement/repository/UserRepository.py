class UserRepository:
    
    DataBase = None

    def __init__(self, dataBase):
        self.dataBase = dataBase
        
    def insertUser(self, user):     #insertUser가 실행이 되면 user객체를 받아서
        data = self.dataBase.getData()     #data를 들고온다
        data.get("user_mst").append(user.toDict()) 
        # -> user 객체를 딕셔너리 객체로 변환해서 user_mst data에 append
        self.dataBase.save()

    def getUserByUsername(self, username):
        data = self.dataBase.getData() 
        userList = data.get("user_mst")
        for user in userList:
            if user.get("username") == username:
                return user

        return None

    def getUserListAll(self):
        data =self.dataBase.getData()
        userList = data.get("user_mst")
        return userList