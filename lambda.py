# total=lambda a,b:a+b
# print((total(5,2)))

# a=[1,2,3,4,5]
# def increment_by_one(n):
#     return n+1

# output=map(increment_by_one,a)
# print(list(output))
# output=map(lambda n:n+1,a)
# print(list(output))
# print(a)

names=["ram","shyam","sita","hari"]
print(list(map(lambda s:s.title(),names)))
print(list(map(str.title,names)))