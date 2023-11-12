import math


class Vector3:
    """
    a vector in Euclidean space.
    """

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

    def __eq__(self, p: "Vector3") -> bool:
        return self.x == p.x and self.y == p.y and self.z == p.z

    def __hash__(self) -> int:
        # this works provided x, y and z are less than 100.
        return self.x + 100 * self.y + 10000 * self.z

    def __add__(self, p: "Vector3") -> "Vector3":
        return Vector3(self.x + p.x, self.y + p.y, self.z + p.z)

    def __sub__(self, p: "Vector3") -> "Vector3":
        return Vector3(self.x - p.x, self.y - p.y, self.z - p.z)

    def len(self) -> float:
        return math.sqrt(self.dot(self))

    def dist(self, p: "Vector3") -> float:
        return (self - p).len()

    def norm(self) -> "Vector3":
        return self.scale(self.len())

    def scale(self, p) -> "Vector3":
        return Vector3(p * self.x, p * self.y, p * self.z)

    def dot(self, p: "Vector3") -> float:
        return self.x * p.x + self.y * p.y + self.z * p.z

    def cross(self, p: "Vector3") -> "Vector3":
        """
        1. A X B = 0 means A and B are parallel
        2. A X B is clockwise quarter turn of A around B
        """
        return Vector3(self.y * p.z - self.z * p.y,
                  self.z * p.x - self.x * p.z,
                  self.x * p.y - self.y * p.x)


# the basis vectors for Euclidean space using ints.
POS_X = Vector3(1, 0, 0)
POS_Y = Vector3(0, 1, 0)
POS_Z = Vector3(0, 0, 1)
NEG_X = Vector3(-1, 0, 0)
NEG_Y = Vector3(0, -1, 0)
NEG_Z = Vector3(0, 0, -1)
ZERO = Vector3(0, 0, 0)
