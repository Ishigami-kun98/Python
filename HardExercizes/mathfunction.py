def cur(f, a):
    #*args = i still don't know what argument u put but is a number or a list of number
    #that i ll pass as argument
    def fc(*args):
        return f(a, *args)
    return fc

def f2(x, y) : 
    return x + y

def f3(x, y, z):
    return x + y + z

if __name__ == "__main__" : 
    a = cur(f2, 3)
    b = cur(f3, 4)
    c = cur(b, 7)
    print((a,b,c))
    print("(cf2 3)({0}) :- {1} (cf3 4) ({2}, {3}) :- {4}" \
        .format(    1,    a(1),          2,   3,     b(2,3)))
    print("((cf3 4) 7)({0}) :- {1}".format(5, c(5)))
    