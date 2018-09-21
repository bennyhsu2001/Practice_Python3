import json

# json_data = '{"name":"eric","age":30}'
# python_obj = json.loads(json_data)
# # print(type(python_obj))
# print(python_obj)
# print(python_obj["name"])
# print(python_obj["age"])

# json_data = '["Tom","Eric","Mary","Fiona"]'
# python_obj = json.loads(json_data)
# print(python_obj)
# print(python_obj[1])  #Eric
# print(python_obj[3])  #Fiona
# for element in python_obj:
#     print(element)

json_data = '[{"name":"eric","age":30},{"name":"tom","age":25},{"name":"mary","age":33}]'
python_data = json.loads(json_data)
print(python_data)

for obj in python_data:
    print("name:{}, age:{}".format(obj['name'],obj['age']))


L1 = ['a','b','c']
print(type(L1))
L1 = json.dumps(L1)
# L1 = str(L1)
print(type(L1),L1)