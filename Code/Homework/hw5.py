#sahil mukesh ambre
#CWID: 20015751

import math


def twoMaxes(L):
    new_l = [[],[]]

    for i in range(len(L)):
        row_max = 0
        for j in range(len(L[i])):
            if L[i][j] > row_max:
                row_max = L[i][j]
        new_l[0].append(row_max)

    row_len = len(L[0])
    for i in range(row_len):
        col_max = 0
        for j in range(len(L)):
            if L[j][i] > col_max:
                col_max = L[j][i]
        new_l[1].append(col_max)

    return new_l


def dictionaryCollector(L):
    new_d = {'int': 0, 'string': ''}

    for i in L:
        if type(i) == int:
            new_d['int'] += i

        if type(i) == str:
            new_d['string'] += i

    return new_d


def selectionSort(L):
    for i in range(len(L) - 1):

        min_value = i
        for j in range(i + 1, len(L)):
            if L[j] < L[min_value]:
                min_value = j

        L[i], L[min_value] = L[min_value], L[i]


class Circle:
    radius = 0

    def __init__(self, radius):
        self.radius = int(radius)

    def __str__(self):
        return "Radius: " + str(self.radius)

    def area(self):
        return round(math.pi * (self.radius ** 2), 2)


class Sphere(Circle):
    radius = 0

    def __init__(self, radius):
        super().__init__(radius)

    def area(self):
        return round(4 * math.pi * (self.radius ** 2), 2)

    def volume(self):
        return round((4 / 3) * math.pi * (self.radius ** 3), 2)


def preciseDivision(a, b):
    if b == 0:
        return float(math.inf)

    quotient = 0
    while a >= b:
        a -= b
        quotient += 1
    return quotient





