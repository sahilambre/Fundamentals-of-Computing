# def shortStrings(L, n):
#     # x = len(L)
#     # return x
#     s = list(filter(lambda s: len(x) > s))
#     return s

# L = ['sahil', 'sahi', 'sah', 'sa', 's']
# n = 4


# print(shortStrings("sahasil"))


def doubleStrings(L):
    s = list(map(lambda k: k * 2, L))
    return s


L = ['aa', 'a', 'bbb']
print(doubleStrings(L))

def shortStrings(L, n):
    s = list(filter(lambda k: len(k) < n, L))
    return s

L = ['sahil', 'sahi', 'sah', 'sa', 's']
n = 3
print(shortStrings(L, n))


def pigLatin(s):
    first_char = s[0]
    remaining_string = s[1::]
    z = remaining_string + first_char + "ay"
    # u = "ay"
    #r = z.append(["ay"])
    #return z
    #print(z, Str(u))
    #print(list(z))
    return list(z)

print(pigLatin("Hello"))
print(pigLatin("Sahil"))

# 2b: Souble Strings 

def doubleString(L):
    return L + L

initial_string = ('a', 'aa', 'bbb')
doubled_string = map(doubleString, initial_string)
print(list(doubled_string))