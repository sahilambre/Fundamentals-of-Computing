#Sahil Mukesh Ambre
#CWID: 20015751

# Question 1
def spiralOrder(L):
    left, right = 0, len(L[0]) - 1
    up, down = 0, len(L) - 1
    ans = []
    step = 0
    while left <= right and up <= down:
        if step % 4 == 0:
            for i in range(left, right + 1):
                ans.append(L[up][i])
            up += 1
        elif step % 4 == 1:
            for i in range(up, down + 1):
                ans.append(L[i][right])
            right -= 1
        elif step % 4 == 2:
            for i in range(right, left - 1, -1):
                ans.append(L[down][i])
            down -= 1
        elif step % 4 == 3:
            for i in range(down, up - 1, -1):
                ans.append(L[i][left])
            left += 1
        step += 1
    return ans

print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))

# Question 2: Write a dictionary inverter

def inverter(D):
    new_D = {}
    for key, value in D.items():
        # if new_D.get(value):
        if value in new_D:
            new_D[value] = [new_D[value]] + [key]
        else:
            new_D[value] = key
    return new_D

print(inverter({1:'a', 2:'b'}))

def twoSum(L,t):
    pass

#Q3: Matrix Multiplication

def matrixMultiply(A, B):
    assert len(A[0]) == len(B),'enter correct matrix'

    ans = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                ans[i][j] += A[i][k] * B[k][j]

    return ans

print(matrixMultiply([[1,2,3],[4,5,6]],[[1,2],[3,4]]))