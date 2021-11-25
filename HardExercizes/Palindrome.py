def palindrome(parola):
    if len(parola) % 2 == 0:
        
        right = parola[int(len(parola)/2):]
        if parola[:int(len(parola)/2)] == right[::-1]:
            return True
    else:
        right = parola[int(len(parola)/2) + 1:]
        if parola[:int(len(parola)/2)] == right[::-1]:
            return True
    return False

def substractLetters(originalWord, toSub):
    wordToSub = set()
    for s in toSub:
        wordToSub.add(s)
    print(wordToSub)
    result = [r for r in originalWord if not r in wordToSub]
    return ''.join(result)

if __name__ == "__main__":
    print(palindrome("aaabbaaa"))
    print(palindrome("aaabaaa"))
    print(substractLetters("askdkjawjdasldwaijdonzxjkcjvsldkhe2178394", "asjdkjawkdjskajawd"))