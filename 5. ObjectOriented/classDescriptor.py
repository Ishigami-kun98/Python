class Descriptor(object):
    '''A descriptor example'''
    def __get__(self, obj, clas = None):
        print({"{0}.get({1},{2})".format(self,obj,clas)})
    def __set__(self, obj, val):
        print("{0}.__set__({1},{2})".format(self, obj, val))
    def __delete__(self, obj):
        print("{0}.__delete__({1})".format(self,obj))
    
class subClass(Descriptor):
    "A class with a single descriptor"
    d = Descriptor()

if __name__ == "__main__":
    cobj = subClass()
    x = cobj.d
    print(x)
    cobj.d = "setting a prova value"
    
    x = cobj.d
    del cobj.d
    x = subClass.d
    subClass.d = "setting a value on class"
    print(x)