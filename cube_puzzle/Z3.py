class Z3:
    """
    integer triplets treated as vectors
    A X B = 0 means A and B are parallel
    A X B is clockwise quarter turn of A around B
    """

    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    # END

    def __str__(self) -> str:
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

    # END

    def __eq__(self, p: "Z3") -> bool:
        return self.x == p.x and self.y == p.y and self.z == p.z

    # END

    def __hash__(self) -> int:
        # this works provided x, y and z are less than 100.
        return self.x + 100 * self.y + 10000 * self.z

    # END

    def __add__(self, p: "Z3") -> "Z3":
        return Z3(self.x + p.x, self.y + p.y, self.z + p.z)

    # END

    def __sub__(self, p: "Z3") -> "Z3":
        return Z3(self.x - p.x, self.y - p.y, self.z - p.z)

    # END

    def scale(self, p: int) -> "Z3":
        return Z3(p * self.x, p * self.y, p * self.z)

    # END

    def cross(self, p: "Z3") -> "Z3":
        return Z3(self.y * p.z - self.z * p.y,
                  self.z * p.x - self.x * p.z,
                  self.x * p.y - self.y * p.x)
    # END

# the base vectors for Z3
POS_X = Z3(1, 0, 0)
POS_Y = Z3(0, 1, 0)
POS_Z = Z3(0, 0, 1)
NEG_X = Z3(-1, 0, 0)
NEG_Y = Z3(0, -1, 0)
NEG_Z = Z3(0, 0, -1)
ZERO = Z3(0, 0, 0)
