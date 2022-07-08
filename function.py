def welcome():
    print("You are welcome!")

#call by reference
welcome()
def product(num1,num2):
    print(num1*num2)
product(5,6)

def addition(num1,num2):
    print(num1+num2)
def subtraction(num1,num2):
    if num1>num2:
        print(num1-num2)
    else:
        print(num2-num1)

a=input("Enter first number")
b=input("Enter second number")
a=int(a)
b=int(b)
addition(a,b)
subtraction(a,b)