# Sahil Mukesh Ambre CWID: 20015751
#Homewrok 2

# Question 1: Implement the dot product.
def length(l):
    '''
    A custom length function which takes a parameter and 
    returns the number of elements present in l
    '''
    counter = 0
    for element in l:
        counter += 1
    return counter

def dot(L, K):
    '''
    Takes two inputs lists L and K and returns the dot prodcuct of of the two vectors.
    if the lists are not equals returns -ve infinity.
    and if the lists are empty then returns a 0
    the input should be in the list format
    '''
    if length(L) != length(K):
        return -float('inf')
    elif length(L) == 0 and length(K) == 0:
        return 0
    elif length(L) == 1 and length(K) == 1:
        return L[0] * K[0]
    else:
        lbeg = L[0]
        kbeg = K[0]
        lrem = L[1:]
        krem = K[1:]
        return (lbeg * kbeg) + dot(lrem, krem)


print(dot([5, 3], [6, 4]))
print(dot([5, 3], [6]))
print(dot([1], [3]))
print(dot([0], [0]))

# Question 2: Write a String Explosion function.
def explode(S):
    '''
    takes the input as S in a string format and returns a list of all of the characters of a string seperated.
    '''
    if length(S) == 0:
        return []
    elif length(S) == 1:
        return [S]
    else:
        beg = S[:1]
        rem = S[1:]
        return [beg] + explode(rem)

print(explode("spam"))
print(explode(""))


# Question 3: Calculate the running average
def runningAverage(L):
    '''
    takes an input L and calculates the running average
    and returns that to the original list
    '''
    sum, avg = 0,0
    for i in range(length(L)):
        sum = sum + L[i]
        avg = sum / (i+1)
        L[i] = avg
    return L

print(runningAverage([1,2,3,4,5]))


# Question 4: Recreate map and filter

# Custom Map
def customMap(f,L):
    '''
    takes two inputs a function f and a list 
    returns the list by doubling it 
    '''
    for i in range(length(L)):
        L[i] = f(L[i])
    return L

def double(n):
    '''
    takes a parameter n and doubles it 
    n should be of integer type
    '''
    return 2 * n

print(customMap(double, [1,2,3]))

#Custom Filter
def customFilter(f,L):
    '''
    takes two inputs a function f and a list 
    and returns a list of even numbers 
    '''
    list = []
    for i in range(length(L)):
        result = isEven(L[i])
        if result:
            list.append(L[i])
    return list   

def isEven(n):
    '''
    takes a parameter n and checks if it is an even number
    it should be an integer
    '''
    return n % 2 == 0

print(customFilter(isEven, [1,2,3,8]))

