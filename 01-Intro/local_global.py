#Global variable
count = 0

def my_function():
    global count 
    count = 10
    print(count)

print(count)
my_function()
print(count)
my_function()