from audioop import add, mul


def calculator(operator,num1,num2):
    def add():
        return num1+num2
    def mul():
        return num1*num2
    if operator=="+":
        return add
    elif operator=="*":
        return mul
a=calculator("+",10,15)
print(a())
b=calculator("*",10,15)
print(b())