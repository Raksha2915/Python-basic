try:
    n1=int(input("Enter num1 "))
    n2=int(input("Enter num2 "))
except ValueError:
    print("Cannot convet to integer")
except NameError:
    print("Variable not defined")
else:
    print(n1+n2)
