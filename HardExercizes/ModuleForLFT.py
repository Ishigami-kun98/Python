import string
def frequentLetter(filePath):
    p = open(filePath)
    letters = string.ascii_lowercase
    s = p.read()
    s = s.replace('\n', '')
    s.lower()
    listFrequency = list()
    for letter in letters:
        #print("The number of {0} that appear in the text file is {1}\
        #   ".format(letter, s.count(letter)))
        listFrequency.append((letter, s.count(letter)))
    return listFrequency
    
def frequentWords(filePath):
    p = open(filePath)
    s = p.read()
    s.lower()
    wordFrequency = dict()
    c = s.replace("\\", " ").split(" ")
    print(c)
    for word in c:
        wordFrequency[word] = c.count(word)
    return wordFrequency