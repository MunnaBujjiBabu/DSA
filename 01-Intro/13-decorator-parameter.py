def repeat(n):   # decorator with argument
    def decorator(func):
        def wrapper(test):
            for _ in range(n):
                func(test)
        return wrapper
    return decorator

@repeat(3)   # pass argument to decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Bujji")
# Output: Hello, Bujji! (printed 3 times)
