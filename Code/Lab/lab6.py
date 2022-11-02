'''
Please write the function transpose(L) which takes in a 2-D list L and transposes the rows and columns.
i.e. transpose([[1,2],[3,4],[5,6]]) -> [[1,3,5],[2,4,6]]
'''

#Sahil Mukesh Ambre CWID:20015751

def transpose(L):
    result = []
    # for i in range(len(L)):
    for i in range(len(L[0])):
        r = []
        for element in L:
            r.append(element[i])
        result.append(r)
        # print(r)
    return result

print(transpose([[1,2], [3,4], [5,6]]))
