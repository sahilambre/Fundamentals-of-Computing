def sum(tups):
    total = 0 
    for element in tups:
        total = total + element 
    return total

print(sum((1,2,3,4)))

def despace(s):
    acc = ''
    for element in s:
        if element != '':
            acc += element 
    return  acc

print(despace('Helloworld!'))

def reverse(s):
    acc = ''
    for i in s:
        acc = i + acc
        #acc = acc + i
        #print(acc)
    return acc
print(reverse('apple'))

def addOne(L):
    acc = []
    for element in L:
        acc.append(element + 1)
    return acc 
print(addOne([1,2,3]))

def addOneInPlace(L):
    for i in range(len(L)):
        L[i] = L[i] + 1

l = [1,2,5]
addOneInPlace(l)
print(l)
