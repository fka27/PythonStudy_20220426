import json 

json_obj = {
    "id" : 20220001,
    "username" : "garam",
    "password" : "1234",
    "hobby" : ["축구", "농구", "골프", "테니스"]

}

with open ('./src/p22_JSON/user.json', 'w', encoding="utf8") as f :
    json_string = json.dump(json_obj, f, indent=4, ensure_ascii=False)
   