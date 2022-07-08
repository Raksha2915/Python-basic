# sum=0

# for i in range(1,16) :
    # print("{}.sum before adding{}".format(i,sum))
    # print(f"{i}.sum before adding{sum}")
    # sum=sum+i
# print(sum)
even=[]
for i in range(0,10):
    num=input("Enter the number: ")
    num=int(num)
    if num%2==0:
        even.append(num)
print(even)
