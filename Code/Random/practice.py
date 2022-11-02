'''
IMPORTANT NOTES 
1. Functions 
2. Accumulator and counter 
3. return and print 
4. fibonacci series 
5. recurssions 
6. slicing 
7. filter out neatives using loops 
8. maps and filter 
9. do home work problems 
10. revise homework problems
11. revise classroom problems (despace, sum of tuples, )
12. factorial using recursion
'''

def function1(x):
    print(x)
    print("still in the function")
    return 2 * x 

a = function1(4)
print(a)


def greet(n):
    '''
    prints a greeting to a person named n
    precondition: n is a string representing a person's name
    '''
    text = "hello " + n + "!"
    print(text)
    #return text

greet('sahil')
print(greet('hi'))

def plus(n):
    '''
    returns the number n + 1

    parameter n: number to add to 
    precondition: n is a number
    '''
    m = n + 1
    print(m)
# print(plus(6))
plus(8)

def greet1(n):
    '''
    prints greetings to name n
    greeting has format 'hello <n>!'
    followed by conversation starter

    parameter n: person to greet
    precondition: n is a string
    '''
    print("Hello " + n + "!")
    print("How are you?")
greet1('Sahil')
# print(greet1('Sahil'))

def despace(s):
    '''
    despace a string 
    remove all the spaces between the words of a string
    '''
    acc = " "
    for element in s:
        if element != ' ':
            acc += element 
    return acc

print(despace('Hello world'))

def sum(tups):
    '''
    calculate the sum of all the elements of the tuple
    '''
    total = 0 
    for element in tups:
        total = total + element 
    return total

print(sum((1,2,3,-4)))

def fact(n): #Recursion 
    '''
    calculate factorial of a given number 
    '''
    if n == 1 or n == 0:
        return 1 
    else:
        return n * fact(n-1)

print(fact(3))


#doubt 

def addOne(L):
    list = []
    for element in L:
        list.append(element + 1)
    return list

print(addOne([1,2,3]))


def addOneInPlace(L):
    for i in range(len(L)):
        L[i] = L[i] + 1

l = [1,2,5]
addOneInPlace(l)
print(l)


def max1(a,b,c):
    '''
    find maximum of 3 numbers
    '''
    if a > b and a > c:
        return "a greater"
    elif a < b and b > c:
        return "b greater"
    else:
        return "c greater"

print(max1(4,2,3))


#doubt 
def max(L):
    list = []
    current_no = L[0]
    for element in L:
        if element > current_no:
            list.append(element)
            current_no = L[0] + 1
        return element 
    return list

print(max([4,2,3]))


def sumOfList(L):           #Recursion
    '''
    Write a Python program to calculate the sum of a list of numbers.
    '''
    if len(L) == 1:
        return L[0]
    else:
        return L[0] + sumOfList(L[1:])

print(sumOfList([1]))

def power(a,b):             #Recursion
    '''
    Write a Python program to calculate the value of 'a' to the power 'b'
    '''
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif a == 0:
        return 0
    else:
        return a * power(a,b-1)

print(power(2,2))


def sumOfSquareOfNumbers(n): #Recursion
    if n == 1:
        return n
    else:
        return n * n + sumOfSquareOfNumbers(n -1)

print(sumOfSquareOfNumbers(10))


def sumOfPosInt(n):         #Recursion 
    '''
    Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0)
    '''
    # Method 1

    # if n == 1 or n == 0:
    #     return n
    # else:
    #     return n + sumOfPosInt(n - 2)

    # Method 2 
    
    if n < 0:
        return 0
    else:
        return n + sumOfPosInt(n - 2)

print(sumOfPosInt(-11))

def explode1(S):     #String Explosion using loops
    list = []
    for element in S:
        list.append(element)
    return list

print(explode1("sahil"))

def length(l):
    counter = 0
    for element in l:
        counter += 1
    return counter

def doubleArray(L):
    if length(L) == 0:
        return []
    elif length(L) == 1:
        return [2 * L[0]]
    else:
        beg = L[:1]
        end = L[1:]
        return [2 * beg[0]] + doubleArray(end)

print(doubleArray([1,2,3]))

def divisiblity(n):
    '''
    Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)
    '''
    # for element in range(1500,2701):
    #     if n // element == 0:
    #         return 

def explode(S):
    if len(S) == 0:
        return []
    elif len(S) == 1:
        return [S]
    else:
        beg = S[:1]
        rem = S[1:]
        return [beg] + explode(rem)

print(explode("Sahil"))

def filterOutNegative(L):
    '''
        Finish the function filterOutNegative(L) that returns a copy of the given list
        WITHOUT negative numbers
        Implement the function specification above.
        e.x.: filterOutNegative([-1,1,-2,2,3]) -> [1,2,3]
    '''
    if L == []:
        return []
    elif L[0] < 0:
        return filterOutNegative(L[1:])
    else:
        return [L[0]] + filterOutNegative(L[1:])
    

print(filterOutNegative([-1,1,-2,2,3]))

def sumLists(L):
    '''
    Write a Python program to sum all the items in a list.
    '''
    sum = 0
    for i in L:
        sum = sum + i
    return sum

print(sumLists([1,2,3,4,-5]))

def multiplyListElements(L):
    '''
    Write a Python program to multiply all the items in a list.
    '''
    total = 1
    for i in L:
        if i in L == 0:
            return 0
        else:
            total = total * i
    return total

print(multiplyListElements([1,2,5,0]))
print(multiplyListElements([-1, 1 ,-1 ]))

print("*****")

def match_words(L):
    '''
    Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Go to the editor 
    Sample List : ['abc', 'xyz', 'aba', '1221']
    Expected Result : 2 
    '''
    counter = 0
    for i in L:
        if len(i) > 2 and i[0] == i[-1]:
            counter = counter + 1 
    return counter


print(match_words(['sahil', 'aba', '121', '123', '111']))

