#Sahil Mukesh Ambre
#CWID: 20015751

# Question 1
def spiral(L):
    pass

# Question 2: Write a dictionary inverter

def inverter(D):
    new_D = {}
    for key, value in D.items():
        if new_D.get(value):
            new_D[value] = [new_D[value]] + [key]
        else:
            new_D[value] = key
    return new_D

print(inverter({1:'a', 2:'b'}))

def twoSum(L,t):
    pass
