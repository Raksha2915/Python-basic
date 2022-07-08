# def function(*args):
#     print(args)

# function("Ram",3,5)

# def welcome(name):
#     print(f"Welcome {name}")

# def greet(func):
#     func("Ram")

# greet(welcome)
# print(type(welcome))

def square(fun,num1,num2):
    return fun(num1,num2)**2
def add(num1,num2):
    return num1+num2
print(square(add,10,15))