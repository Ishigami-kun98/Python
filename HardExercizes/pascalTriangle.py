class pascalTriangle:
    def __init__(self, maxRow) :
        self.__maxRow = maxRow
        self.trianglePascal = [[1], [1, 1]]
    def __iter__(self):
        self.__current = 1
        return self
    def __next__(self):
        print(self.__current)
        if self.__current > self.__maxRow: raise StopIteration
        print(self.trianglePascal[len(self.trianglePascal) -1])
        prova = secondIterator(self.trianglePascal[len(self.trianglePascal) -1])
        #to fix the above one
        secondary = []
        for i in prova:
            secondary.append(i)
        self.trianglePascal.append(secondary)
        self.__current+=1

    def __prev__(self):
        pass

class secondIterator:
    def __init__(self, listTop) -> None:
        self.__listTop = listTop
    def __iter__(self):
        self.__currentPosition = 1
        self.__result = []
        self.__result.append(1)
        return self
    def __next__(self):
        #print(len(self.__listTop))
        if len(self.__listTop) == self.__currentPosition :
            self.__result.append(1)
            raise StopIteration
        if len(self.__listTop) >= 2:
            calc = self.__listTop[self.__currentPosition] + self.__listTop[self.__currentPosition -1]
            self.__result.append(calc)
        self.__currentPosition += 1

if __name__ == "__main__":
    PT = pascalTriangle(5)
    for i in PT: print(i)