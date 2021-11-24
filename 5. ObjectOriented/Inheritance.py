from Rectangle import rectangle

class square(rectangle):
    def __init__(self, width):
        self._width = width
        self._height = width
    def __str__(self):
        return "I'm a Square, my side is : {0}\n \
            my Area is {1}".format(self._width, self.calculate_area())

if __name__ == "__main__":
    shapes = [square(7), rectangle(2,4), square(10), rectangle(7,4)]
    print(shapes)
    for shap in shapes:
       print(shap)