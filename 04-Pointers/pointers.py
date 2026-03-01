import ctypes
num1 = 11
num2 = num1

print("value of num1", num1)
print("value of num2", num2)


print("address of num1", id(num1))
print("address of num2", id(num2))


num2 = 22

print("value of num1", num1)
print("value of num2", num2)


print("address of num1", id(num1))
print("address of num2", id(num2))

addr = id(num1)
data = ctypes.cast(addr, ctypes.py_object).value
print(data)



dict1 = {"name": "Alice", "age": 30}
dict2 = dict1



print(dict1)
print(dict2)


print(id(dict1))
print(id(dict2))


dict2["name"] = "Munna"


print(dict1)
print(dict2)



print(id(dict1))
print(id(dict2))