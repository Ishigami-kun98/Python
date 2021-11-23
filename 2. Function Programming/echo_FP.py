def monadic_print(x):
    print(x)
    return x
echo_FP = \
    lambda: monadic_print(input("FP --")) == "quit" or echo_FP
if __name__ == "__main__" : echo_FP()