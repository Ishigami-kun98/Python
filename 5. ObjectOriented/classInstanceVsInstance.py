class z:
    def __init__(self):
        self.class_attribute = "a value"
    def __str__(self) -> str:
        return self.class_attribute

if __name__ == "__main__":
    prova = z()
    print(prova)
    print(prova.class_attribute)
    prova2 = z()
    prova2.instance_attribute = 199
    z.another_class_attribute = "another value"
    print((prova.another_class_attribute, prova2.another_class_attribute))
    #use dict
    print((prova.__dict__, prova2.__dict__))
    prova2.__dict__["instance_attribute"] = "cambio valore"
    print(prova2)