# def example(**kwargs):
#     print(kwargs)

# example(name="Ram",age=19,address="Budhanilkantha")

# def example(*args,**kwargs):
#     print(kwargs)
#     print(args)

# example(1,2,3,name="Ram",age=19,address="Budhanilkantha")

def example(name,age,address):
    print(f"Name={name}")
    print(f"Age={age}")
    print(f"Address={address}")

pro={"name":"Ram","age":19,"address":"Budhanilkantha"}
example(**pro)