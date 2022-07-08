total=0
n="12d567d895d56"
a=n.split("d")
print(a)
for i in a:
    total+=int(i)
print(total)
#total=sum([int(i) for i in n.split("d")])
# for i in range()