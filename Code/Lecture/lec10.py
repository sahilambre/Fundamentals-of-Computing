'''
    repr()
    #In addition tp raising an ArithmaticError
    if matrix are valid
    you can also assert that the dimension are valid
    either arithmetic or assertion no other error 
    AssertionError or ArithmeticError
'''

def double(n):
    '''
        given a number n double it 
    '''
    assert type(n) == int or type(n) == float, 'Enter either integer or float'
    return n * 2

print(double(""))
