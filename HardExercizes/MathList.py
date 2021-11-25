from math import gcd
def sumMultiple():
    return sum([x for x in range(0,1000,3) if x % 5 == 0])

def minComuneMultiple():
    test = [11,12,13,14,15,16,17,18,19,20]
    lcm = 1
    for i in test:
        lcm = lcm*i//gcd(lcm, i)
    return lcm
def cifredueallamille(n):
    lunghezza = str(n)
    return len(lunghezza)

def fibMilleCifre():
    a,b = 0, 1
    condition = True
    while(condition):
        a, b = b, a + b
        if(len(str(a)) == 1000): condition = False
    return a 

if __name__ == "__main__":
    print(sumMultiple())
    print(minComuneMultiple())
    print(cifredueallamille(2**1000))
    print(fibMilleCifre())
    