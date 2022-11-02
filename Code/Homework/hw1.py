# Sahil Mukesh Ambre CWID: 20015751

# Question 1: Write Temperature Converting Functions 
def fToC(t):
    c = (t - 32) * 5/9
    return c

def cToF(t):
    f = (t * 9/5) + 32
    return f

print(fToC(72))
print(cToF(22.22))


# Question 2: Test out map and filter 
# 2a: Short Strings
def shortStrings(L, n):
    s = list(filter(lambda k: len(k) < n, L))
    return s

L = ['a', 'b', 'abcde', 'abcdef', 'abc']
n = 3
print(shortStrings(L, n))


# 2b: Double Strings 
def doubleStrings(L):
    s = list(map(lambda k: k * 2, L))
    return s

L = ['aa', 'a', 'bbb', 'b', 'c']
print(doubleStrings(L))


# Question 3: Pig Latin
def pigLatin(s):
    first_char = s[0]
    remaining_string = s[1::]
    z = remaining_string + first_char + "ay"
    return list(z)

print(pigLatin("hello"))
print(pigLatin("Sahil"))
