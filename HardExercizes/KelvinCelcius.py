def fromKelvin(x):
    return x
def toKelvin(x):
    return x
def fromCelsius(x):
    return x - 273.15
def toCelsius(x):
    return x + 273.15

def toFahrenheit(x):
    return x + 459.67
def fromFahrenheit(x):
    return x - 459.67

patterns = [(fromKelvin, toKelvin), (fromCelsius, toCelsius), (fromFahrenheit, toFahrenheit)]
scales = ["Kelvin", "Celsius", "Fahrenheit"]
def table(x):
    for fromtemp, totemp in patterns:
        print(totemp(x))
        print(fromtemp(x))

def toAll(x, scale):
    pos = scales.index(scale)
    scaleFind = patterns[pos]
    table(scaleFind[0](x))

        
if __name__ == "__main__":
    table(10)
    toAll(10, "Fahrenheit")