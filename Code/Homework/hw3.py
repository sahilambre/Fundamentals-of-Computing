#Sahil Mukesh Ambre
#CWID: 20015751

# Question 1: Spiral 

def spiral(L):
    up_pointer, down_pointer = 0, len(L) - 1
    left_pointer, right_pointer = 0, len(L[0]) - 1
    
    step = 0
    answer = []
    
    while left_pointer <= right_pointer and up_pointer <= down_pointer:
        if step % 4 == 0:
            for i in range(left_pointer, right_pointer + 1):
                answer.append(L[up_pointer][i])
            up_pointer = up_pointer + 1
        elif step % 4 == 1:
            for i in range(up_pointer, down_pointer + 1):
                answer.append(L[i][right_pointer])
            right_pointer = right_pointer - 1
        elif step % 4 == 2:
            for i in range(right_pointer, left_pointer - 1, -1):
                answer.append(L[down_pointer][i])
            down_pointer = down_pointer - 1
        elif step % 4 == 3:
            for i in range(down_pointer, up_pointer - 1, -1):
                answer.append(L[i][left_pointer])
            left_pointer = left_pointer + 1
        step = step + 1
    
    return answer

# print(spiral([[1,2,3],[4,5,6],[7,8,9]]))

# Question 2: Write a dictionary inverter

def inverter(D):
    new_Dict = {}
    for key, value in D.items():
        if new_Dict.get(value):
        #if value in new_D:
            new_Dict[value] = [new_Dict[value]] + [key]
        else:
            new_Dict[value] = key
    return new_Dict

# print(inverter({1:'a', 2:'b'}))
# print(inverter({1:'a', 2:'b', 3:'a'}))

# Question 3: Matrix Multiplication

def matrixMultiply(A, B):
    assert len(A[0]) == len(B),'Incorrect Matrix Dimesions'

    ans = [[0 for X in range(len(B[0]))] 
        for X in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                ans[i][j] += A[i][k] * B[k][j]

    return ans

# print(matrixMultiply([[1,2,3],[4,5,6]],[[1,2],[3,4], [5,6]]))

# Question 4: Two Sum

def twoSum(L, t):
    answer = []
    new_dict = {}
    
    for s in range(len(L)):
        if t - L[s] in new_dict:
            answer.append(tuple((L[new_dict.get(t - L[s])], L[s])))

        new_dict[L[s]] = s

    return answer

# print(twoSum([1,2,3,4,4,3,4,5], 6))