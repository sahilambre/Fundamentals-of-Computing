#Sahil Mukesh Ambre
# from unittest import result
import introcs
def numberAnalysis(n):
    if n > 0:
        return n * 2
    elif n < 0:
        return numberAnalysis(n * -1)
    elif n == 0:
        return -1

print(numberAnalysis(3))
print(numberAnalysis(-1))
print(numberAnalysis(0))

def testCases():
    res = numberAnalysis(3)
    introcs.assert_equals(6,res)
    res1 = numberAnalysis(-1)
    introcs.assert_equals(2,res1)
    res2 = numberAnalysis(0)
    introcs.assert_equals(-1,res2)

testCases()