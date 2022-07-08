# def outer():
#     def first():
#         print("I am the first")
#     def second():
#         print("I am the second")
#     second()
#     first()
# outer()

def calculator(operator):
    def add(a,b):
        return a+b
    def product(a,b):
        return a*b
    if operator == "+":
        return add
    elif operator =="*":
        return product
tsum=calculator("+")
multip=calculator("*")
print(tsum(10,10))
print(multip(10,11))

