#Sahil Mukesh Ambre
def sumOfSquares(n):
    if n == 1:
        return 1
    else:
        return n * n + sumOfSquares(n-1)


print(sumOfSquares(10))