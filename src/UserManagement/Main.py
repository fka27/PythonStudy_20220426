from controller.AuthControllar import AuthController
from service.UserService import UserService
from repository.UserRepository import UserRepository
from repository.DataBase import DataBase

dataBase = DataBase()
userRepository = UserRepository(dataBase)
userService = UserService(userRepository)
authController = AuthController(userService)
authController.index()
