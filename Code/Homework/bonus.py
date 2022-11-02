def stringBalance(s):
    stringAsList = list(s)
    def firstHalf(c):
        return ord(c) < ord('m')
    def secondHalf(c):
        return ord(c) > ord('m')
    firstHalf = list(filter(firstHalf, stringAsList))
    secondHalf = list(filter(secondHalf,  stringAsList))
    return len(secondHalf) - len(firstHalf)
print(stringBalance('azaza'))

