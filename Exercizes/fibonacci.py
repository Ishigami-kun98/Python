def gfib(max):
    a, b = 0, 1
    while a < max :
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    number = int(input('insert a max value of fibonacci function: '))
    for n in gfib(number):
        print(n, end=' ')
