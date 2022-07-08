# a=[1,2,3,4,5]
# output=list(filter(lambda n:n%2!=0,a))
# print(output)

# emails=[
#     "1@gmail.com",
#     "2@yahoo.com",
#     "3@gmail.com",
#     "4@outlook.com",
#     "5@gmail.com",
#     "gmail.com67"
# ]
# out=list(filter(lambda s:s.endswith("@gmail.com"),emails))
# print(out)

a=[1,2,3,"python","apple",5,6,7]
out=sum(filter(lambda n:isinstance(n,int),a))
print(out)