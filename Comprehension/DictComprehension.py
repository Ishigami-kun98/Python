dict = dict()
dict["ciao"] = "helloworld"
dict["ciao1"] = "helloworld1"
dict["ciao2"] = "helloworld2"
dict["ciao3"] = "helloworld3"
print(dict)
print("swap the key : value")
print({key:value for value, key in dict.items()})

atoe = ['a','b','c','d','e']
stoz = ['s','t','u','v','z']
print(atoe)
print(stoz)
print({atoe[x] : stoz[x] for x in range(0,len(atoe))})
