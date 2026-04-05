import json

my_dict = {'name': "munna", 'age': 40}
my_json = json.dumps(my_dict)
print(my_dict)
print(my_json)



my_json = '{"name": "munna", "age": 40}'
my_python_object = json.loads(my_json)



print(type(my_python_object))
print(my_python_object)