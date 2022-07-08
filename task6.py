heros=["spider man","thor","hulk","iron man","captain america"]
print(len(heros))#printing the length of heros
heros.append("black panther")
print(heros)#appending black panther at the end
heros.remove("black panther")
heros.insert(3,"black panther")
print(heros)#adding black panther after hulk
heros[1:3]=["doctor strange"]#adding doctor strange by removing thor and hulk
print(heros)
heros.sort()#sorting in ascending order
print(heros)
