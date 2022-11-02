# Sahil Mukesh Ambre

def stringBalance(s):
    i = 0
    for element in s:
        if ord(element) < ord('m'):
           i = i - 1
        else:
            i = i + 1
    return i
        
    

print(stringBalance('azazaz'))
print(stringBalance('azazazaa'))
print(stringBalance('azazazzz'))

