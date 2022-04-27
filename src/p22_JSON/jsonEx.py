import json  #시작은{},""문자열로 묶어주기, 콤마사용, 객체로 묶을 때 {}

user_json='''{
    "company" : "kakao",
    "users" : [{
        "usercode" : "20220001",
        "username" : "garam",
        "password" : "1111",
        "name" : "김가람",
        "email" : "rkfka0227@gmail.com"
        },{
        "usercode" : "20220002",
        "username" : "garam2",
        "password" : "2222",
        "name" : "김가람2",
        "email" : "rkfka0228@gmail.com"
        }
    ]
}'''

user_json_obj = json.loads(user_json)

print(user_json_obj)
print(type(user_json_obj))


print(f'회사명: {user_json_obj.get("company")}')
userList = user_json_obj.get("users")
print(f'첫번째 사원의 정보: {userList[0]}')

print(f'두번째 사원의 정보: {userList[1]}')
