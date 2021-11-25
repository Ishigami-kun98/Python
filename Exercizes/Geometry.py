class geometry:
    def __init__(self):
        pass
    def calculate_area(self):
        pass
    def calculate_perimeter(self):
        pass
    def __str__(self) -> str:
        return "Area is {0} and the perimeter is {1}".format(self.calculate_area(), self.calculate_perimeter())
    
class trangles(geometry):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__name = "triangles"
    def calculate_area(self):
        return (self.__width * self.__height)/2
    def calculate_perimeter(self):
        return self.__width + self.__height
    def getName(self):
        return self.__name

class rectangles(geometry):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__name = "rectangles"
    def calculate_area(self):
        return self.__width * self.__height
    def calculate_perimeter(self):
        return self.__width + self.__height
    def getName(self):
        return self.__name
class squares(geometry):

    def __init__(self, width):
        self.__width = width
        self.__name = "squares"
    def calculate_area(self):
        return (self.__width ** 2)
    def calculate_perimeter(self):
        return self.__width * 4
    def getName(self):
        return self.__name

#Too lazy to implement it ehee ;)
class pentagons(geometry): 
    def __init__(self, width):
        self.__width = width
    def calculate_area(self):
        return (self.__width ** 2)
    def calculate_perimeter(self):
        return self.__width * 4 
    def getName(self):
        return self.__name
class iterGeometry:
    def __init__(self, geometryList) -> None:
        self.__dictList = geometryList
    def __iter__(self):
        self.__index = -1
        return self
    def __next__(self):
        self.__index+=1
        if len(self.__dictList) <= self.__index:
            raise StopIteration
        return self.__dictList[self.__index]
    

    
if __name__ == "__main__":
    triangle = trangles(20,40)
    rectangle = rectangles(20,40)
    square = squares(20)
    geometri = [triangle, rectangle,square]
    dictionary = dict()
    for i in geometri:
        #print("Area is {0} and the perimeter is {1}".format(i.calculate_area(), i.calculate_perimeter()))
        print(i)
    iteratore = iterGeometry(geometri)
    for i in iteratore:
        print(i)
    
        
