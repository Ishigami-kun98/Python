alkaline_earth_metals = [("barium", 56), ("beryllium", 4), ("calcium", 20), ("magnesium", 12)]
"""maxAlkaline = ""
maxN = 0
for a, b in alkaline_earth_metals:
    if(b > maxN):
        maxN = b
        maxAlkaline = a
print((maxAlkaline, maxN))
"""
print(sorted(alkaline_earth_metals, key=lambda x:x[1], reverse = True)[0][1])
print(sorted(alkaline_earth_metals, key=lambda x:x[1]))

dictionary = {a:b for a,b in alkaline_earth_metals}
#dictionary = dict(alkaline_earth_metals)
print(dictionary)
alkaline_earth_metals2 = {"helioum" : 2, "neon":10, "argon":18, "krypton" : 36}
newDict = dict()
newDict.update(dictionary)
newDict.update(alkaline_earth_metals2)
print(newDict)