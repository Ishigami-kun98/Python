class PolishCalculator:
    def __init__(self, arthexp):
        self.__arthexp = arthexp
    def __str__(self) -> str:
        return "The expression entered is {0} and the result eval is \
            ".format(self.__arthexp, self.eval(self.__arthexp))
    def eval(self, exp):
        pass