main=[]
even=[]
odd=[]
duplicate=[]
for i in range(15):
    num=int(input("Enter the number:"))
    if num not in main:
        if num%2==0:
            even.append(num)
        else:
            odd.append(num)
    else:
        duplicate.append(num)
    main.append(num)
print(main)
print(even)
print(odd)
print(duplicate)

