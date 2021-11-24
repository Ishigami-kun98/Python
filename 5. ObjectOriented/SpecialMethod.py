class SpecialMethod(object):
    #called when u use len
    def __len__(self):
        return self.mylen
    #appen su una lista di int modificabile ofc
    def append(self, item):
        list.append(self, int(item))
    def __setitem__(self, key, item):
        list.__setitem__(self, key, int(item))