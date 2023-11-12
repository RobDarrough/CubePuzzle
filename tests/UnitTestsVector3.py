import math

from cube_puzzle.Vector3 import Vector3 as Vector3
from cube_puzzle.Vector3 import POS_X as POS_X
from cube_puzzle.Vector3 import POS_Y as POS_Y
from cube_puzzle.Vector3 import POS_Z as POS_Z
from cube_puzzle.Vector3 import NEG_X as NEG_X
from cube_puzzle.Vector3 import NEG_Y as NEG_Y
from cube_puzzle.Vector3 import NEG_Z as NEG_Z
from cube_puzzle.Vector3 import ZERO as ZERO

# def __str__(self) -> str:

assert str(POS_X) == "(1, 0, 0)"
assert str(POS_Y) == "(0, 1, 0)"
assert str(POS_Z) == "(0, 0, 1)"
assert str(NEG_X) == "(-1, 0, 0)"
assert str(NEG_Y) == "(0, -1, 0)"
assert str(NEG_Z) == "(0, 0, -1)"
assert str(ZERO) == "(0, 0, 0)"

# def __eq__(self, p: "Vector3") -> bool:

assert POS_X == Vector3(1, 0, 0)
assert POS_Y == Vector3(0, 1, 0)
assert POS_Z == Vector3(0, 0, 1)

# def __add__(self, p: "Vector3") -> "Vector3":

assert POS_X + NEG_X == ZERO
assert POS_Y + NEG_Y == ZERO
assert POS_Z + NEG_Z == ZERO
assert POS_X + POS_Y + POS_Z + NEG_X + NEG_Y + NEG_Z == ZERO

# def __sub__(self, p: "Vector3") -> "Vector3":

assert POS_X - POS_X == ZERO
assert POS_Y - POS_Y == ZERO
assert POS_Z - POS_Z == ZERO
assert ZERO - POS_X - POS_Y - POS_Z - NEG_X - NEG_Y - NEG_Z == ZERO

# def dot(self, p: "Vector3") -> float:

assert POS_X.dot(POS_X) == 1.0
assert POS_Y.dot(POS_Y) == 1.0
assert POS_Z.dot(POS_Z) == 1.0

assert NEG_X.dot(NEG_X) == 1.0
assert NEG_Y.dot(NEG_Y) == 1.0
assert NEG_Z.dot(NEG_Z) == 1.0

assert NEG_X.dot(POS_X) == -1.0
assert POS_Y.dot(NEG_Y) == -1.0
assert NEG_Z.dot(NEG_Z) == 1.0

# def len(self) -> float:

assert POS_X.len() == 1.0
assert POS_Y.len() == 1.0
assert POS_Z.len() == 1.0

assert NEG_X.len() == 1.0
assert NEG_Y.len() == 1.0
assert NEG_Z.len() == 1.0

assert (POS_X + POS_Y).len() == math.sqrt(2.0)
assert (POS_Y + POS_Z).len() == math.sqrt(2.0)
assert (POS_Z + POS_X).len() == math.sqrt(2.0)

# def dist(self, p: "Vector3") -> float:

assert POS_X.dist(NEG_X) == 2.0
assert POS_Y.dist(NEG_Y) == 2.0
assert POS_Z.dist(NEG_Z) == 2.0

assert POS_X.dist(POS_Y) == math.sqrt(2.0)
assert POS_Y.dist(POS_Z) == math.sqrt(2.0)
assert POS_Z.dist(POS_X) == math.sqrt(2.0)

assert NEG_X.dist(NEG_Y) == math.sqrt(2.0)
assert NEG_Y.dist(NEG_Z) == math.sqrt(2.0)
assert NEG_Z.dist(NEG_X) == math.sqrt(2.0)

# def norm(self) -> "Vector3":

assert (POS_X + POS_Y).norm() == Vector3(math.sqrt(2.0), math.sqrt(2.0), 0.0)
assert (POS_Y + POS_Z).norm() == Vector3(0.0, math.sqrt(2.0), math.sqrt(2.0))
assert (POS_X + POS_Z).norm() == Vector3(math.sqrt(2.0), 0.0, math.sqrt(2.0))

assert (NEG_X + NEG_Y).norm() == Vector3(-math.sqrt(2.0), -math.sqrt(2.0), 0.0)
assert (NEG_Y + NEG_Z).norm() == Vector3(0.0, -math.sqrt(2.0), -math.sqrt(2.0))
assert (NEG_X + NEG_Z).norm() == Vector3(-math.sqrt(2.0), 0.0, -math.sqrt(2.0))

# def scale(self, p) -> "Vector3":

assert (POS_X + POS_Y + POS_Z).scale(3.0) == Vector3(3.0, 3.0, 3.0)
assert (NEG_X + NEG_Y + NEG_Z).scale(3.0) == Vector3(-3.0, -3.0, -3.0)

# def cross(self, p: "Vector3") -> "Vector3":

assert POS_X.cross(POS_Y) == POS_Z
assert POS_Y.cross(POS_Z) == POS_X
assert POS_Z.cross(POS_X) == POS_Y
assert NEG_Y.cross(NEG_X) == NEG_Z
assert NEG_Z.cross(NEG_Y) == NEG_X
assert NEG_X.cross(NEG_Z) == NEG_Y
