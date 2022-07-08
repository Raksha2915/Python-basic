username="r@gmail.com"
password="123@abcd"
while True:
    user=input("Enter the username")
    passw=input("Enter the password")
    x=user.casefold()
    y=username.casefold()
    a=passw.casefold()
    b=password.casefold()
    if x==y and a==b:
        print("Same user name and password")
        print("Logged in")
        break
    print("Enter username and password again!")


