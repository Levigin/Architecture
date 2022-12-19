import math


class Polygon:
    """
    class Polygon


    Attributes:
        points: list
        tuple coordinates created polygon's

    Method:
        __init__:
            constructor class
        __str__:
            :return str
        __repr__:
            :return representation

    """

    def __init__(self, points: list):
        if len(points) < 3:
            raise Exception("You don't create polygon with point less 3")
        self.points = list(sorted(points, key=lambda p: (p.x, p.y, p.z)))
        print(self.points)

    def __str__(self):
        s = ''
        for i in self.points:
            s += f'{str(i)}'
        return s

    def __repr__(self):
        return str(self)


class Point3D:
    """
    class Point3D:
        class save coordinate's point

    Arguments:
        x: int
        y: int
        z: int

    Method:
        get_distance:
            get distance between points with coordinates (x,y,z)
    """

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return f'{(self.x, self.y, self.z)}'

    def __repr__(self):
        return f'{(self.x, self.y, self.z)}'

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        i = self.index
        self.index += 1
        return i

# point1 = Point3D(1, 24, 46)
# point2 = Point3D(2, 532, 12)
# point3 = Point3D(3632, 2, 1)
# t = [point1, point2, point3]
# polygon = Polygon(t)
