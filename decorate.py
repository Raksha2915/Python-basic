# def decoratefun(fun):
#     def wrapper():
#         print("I am the first")
#         fun()
#         print("I am the second")
#     return wrapper

# @decoratefun
# def welcome():
#     print("Welcome")
# welcome()
# print(welcome)

# def outer(func):
#     def inner():
#         print("Hello!")
#         func()
#     return inner
# @outer
# def welcome():
#     print("Welcome")
# welcome()
#reference of welcome is assigned to the inner()


def smart_division(func):
    def wrapper(a,b):
        if b==0:
            return "not divided"
        else:
            return func(a,b)
    return wrapper
@smart_division
def division(a,b):
    return a/b
print(division(10,2))
print(division(10,0))
