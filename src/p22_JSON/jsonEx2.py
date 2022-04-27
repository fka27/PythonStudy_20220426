import json 

with open('./src/p22_JSON/company.json',encoding="utf_8") as f:
    json_obj = json.load(f)

print(json_obj)
print(type(json_obj))
