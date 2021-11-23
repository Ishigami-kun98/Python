import math, functools

def odd(x):
    return x%2 != 0
def sum(x, y):
    return x + y;

if __name__ == "__main__":
    print(math.sqrt(9))
    print(list(map(math.sqrt, [x**2 for x in range(1,11)])))
    print(list(filter(odd, range(1,50))))
    print(functools.reduce(sum, range(1000)))
    block = lambda s: s
    cond = \
        lambda x: \
            (x==1 and block("one")) or (x==2 and block("two")) or (block("other"))
    print("cond({0}) :- {1}".format(3,cond(3)))
    print("cond({0}) :- {1}".format(2,cond(2)))
    sumLambda = lambda i,j : i + j
    oddLambda = lambda i : i % 2 != 0
    print(sumLambda(2,3))
    print(oddLambda(3))