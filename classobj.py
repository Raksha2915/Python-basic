# class Car:
#     def __init__(self,model,color):
#         self.m=model
#         self.c=color
# c=Car("2020","Black")
# print(c.m)
# print(c.c)

#Book->class
#page->attribute
#read->method

# class Book:
#     def __init__(self,page):
#         self.p=page
#     def read(self):
#         print(f"read page {self.p}")

# b=Book("20")
# # b.read()
# Book.read(b)
# c=Book("21")
# c.read()

class Page:
    def __init__(self,pageno,content):
        self.pageno=pageno
        self.content=content

    def read(self):#instance method
        print(f"Reading {self.content} from page {self.pageno}")
    @staticmethod#static method
    def print_to_printer(content):
        print(f"Printing....")
        print(content)
    def __repr__(self):
        return self.content

# p=Page(1,"paragraph 1st")
# p.read()
# Page.print_to_printer("paragraph 2nd")


class Book:
    def __init__(self,title,pages):
        self.title=title
        self.pages=pages
    def num_of_pages(self):
        return len(self.pages)
    def add_page(self,page):
        self.pages.append(page)
    def __str__(self):
        return self.title
    def get_content(self,pageno):
        for i in self.pages:
            if i.pageno==pageno:
                return i.content
            else:
                return "Not found"
pages=[]
for i in range(1,6):
    p=Page(i,f"This is paragraph {i}.")
    pages.append(p)
b=Book("Maths",pages)
# print(f"Number of pages:{b.num_of_pages()}")

p=Page(6,"New page")
b.add_page(p)
# print(f"Number of pages:{b.num_of_pages()}")
print(b)
print(p)
print(b.pages)
print(b.get_content(10))
print(b.__dict__)