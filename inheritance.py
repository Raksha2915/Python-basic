from re import S


class User:
    def __init__(self,id,username,pwd):
        self.id=id
        self.username=username
        self.password=pwd

    def login(self,uname,pwd):
        if self.username==uname and self.password==pwd:
            return "logged in successfully"
        return "Unauthorised user"

class Teacher(User):
    def __init__(self, id, username, pwd,designation):
        super().__init__(id, username, pwd)
        self.designation = designation

class Student(User):
    def __init__(self,id,username,pwd,faculty):
        super().__init__(id,username,pwd)
        self.faculty = faculty

t=Teacher(1,"teacher","teacher","professor")
s=Student(1,"student","student","BCT")
uname=input("Enter your username:")
pwd=input("Enter your password:")
# print(t.login(uname,pwd))
print(s.login(uname,pwd))
