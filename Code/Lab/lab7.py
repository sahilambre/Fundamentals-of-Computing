#Sahil Mukesh Ambre
#20015751

from introcs import Point3

def manhattanDistance(p0, p1):
    '''
        Given two introcs Point3s,
        return their Manhattan distance

        Manhattan distance is the purely axial distance (distance with no diagnols)

        1  2  5
        3  4  6

        point3(1,1,1)
        point3(2,5,-1)
        7
    '''
    return abs(p1.x - p0.x) + abs(p1.y - p0.y) + abs(p1.z - p0.z)

x = Point3(1,1,1)
y = Point3(2,5,-1)
print(manhattanDistance(x,y))
