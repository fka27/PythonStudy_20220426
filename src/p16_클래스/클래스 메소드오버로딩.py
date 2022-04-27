from multipledispatch import dispatch
#콘솔 창에 pip install multopledispatch 입력 후 프로그램 재실행


class User:
    username = ""
    password = ""
    name = ""

    # @->어노테이션(디스패치)
    def showUserInfo(self):
        print(f"username: {self.username}")
        print(f"password: {self.password}")
        print(f"name: {self.name}")

    @dispatch(str)
    def addUser(self, username):
        self.username = username

    @dispatch(str, str)
    def addUser(self, username, password):
        self.username = username
        self.password = password
 
    @dispatch(str, int)
    def addUser(self, username, password):
        self.username = username
        self.password = str(password)

    @dispatch(str, str, str)
    def addUser(self, username, password, name):
        self.username = username
        self.password = password
        self.name = name

    @dispatch(str, int, str)
    def addUser(self, username, password, name):
        self.username = username
        self.password = str(password)
        self.name = name
#1
user1 = User()
user1.addUser("garam")
user1.showUserInfo()

#2
user2 = User()
user2.addUser("garam", 1234)
user2.showUserInfo()

#3
user3 = User()
user3.addUser("garam2", 3214, "김가람")
user3.showUserInfo()











