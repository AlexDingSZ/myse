import  json

jsondict = {"name":"mytest", "type":{"name":"type_name", "other_para":["1", "2"]}}
python_string = json.dumps(jsondict)
print(python_string)
print(jsondict)

print(type(python_string))
print(type(jsondict))

string_to_json=json.loads(python_string)
print(string_to_json)
print(type(string_to_json))

print(string_to_json.keys())
print(string_to_json["name"])
print(string_to_json["type"]["name"])
print(string_to_json["type"]["other_para"][0])