class shape:
    def calculate_area(self): pass
    def calculate_perimeter(self): pass
    def __str__(self): pass

class rectangle(shape):
    def __init__(self, width, height):
        self._width = width
        self._height = height
    def calculate_area(self):
        return self._width * self._height
    def calculate_perimeter(self):
        return 2*(self._height + self._width)
    
    def __str__(self):
        return "I m a rectangle, my sides are {0}, {1}\nMyArea is {2}".\
            format(self._width, self._height, self.calculate_area())


if __name__ == "__main__":
    r = rectangle(7,42)
    print(r)