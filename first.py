# print("Hey Python!")
# num1=input("Enter 1st number ")
# num2=input("Enter 2nd number ")
# num1=int(num1)
# num2=int(num2)
# num=num1+num2
# print(num)

num=input("Enter any number ")
num=int(num)
if num%3==0:
    print("Divisible by 3")
if num%5==0:
    print("Divisible by 5")
if num%7==0:
    print("Divisible by 7")
else:
    print("Divisible by none")
