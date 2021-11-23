def cond(x):
    return (x==1 and 'one') or (x==2 and 'two') or 'other'

if __name__ == "__main__":
    for i in range(3):
        print("cond({0}) :- {1}".format(i, cond(i)))
