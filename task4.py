sum=0
a=[('1','2','3'),('5','6','7'),('8','9','0')]
for i in range(3):
    n=a[i:i+1]
    x=''.join(n)
    sum=sum+int(x)
    print(n)
print(sum)

