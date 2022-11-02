def numEs(s):
    if s == '':
        return 0
    firstLetter = s[0]
    theRest = s[1:]
    if firstLetter == 'e':
        return 1 + numEs(theRest)
    else:
        return 0 + numEs(theRest)

print(numEs("lll"))