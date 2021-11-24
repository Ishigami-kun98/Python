class odd:
    def __init__(self, max):
        self.max = max
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        self.a += 2
        if(self.a >= self.max): raise StopIteration
        
        return self.a

if __name__ == "__main__":
    c = odd(30)
    for i in c:
        print(i)