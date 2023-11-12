from cube_puzzle.Vector3 import Vector3 as Vector3
from cube_puzzle.Vector3 import POS_X as POS_X
from cube_puzzle.Vector3 import POS_Y as POS_Y
from cube_puzzle.Vector3 import POS_Z as POS_Z
from cube_puzzle.Vector3 import NEG_X as NEG_X
from cube_puzzle.Vector3 import NEG_Y as NEG_Y
from cube_puzzle.Vector3 import NEG_Z as NEG_Z
from cube_puzzle.Vector3 import ZERO as ZERO
from cube_puzzle.AtomicCube import AtomicCube as AtomicCube


# this is the default ordering of the axes. it is used in the string representation.
# AXES = (POS_X, NEG_X, POS_Y, NEG_Y, POS_Z, NEG_Z)

cubes = {"000": AtomicCube(0, 0, 0), "NNN": AtomicCube(-1, -1, -1), "NNP": AtomicCube(-1, -1, 1),
         "NPN": AtomicCube(-1, 1, -1), "NPP": AtomicCube(-1, 1, 1), "PNN": AtomicCube(1, -1, -1),
         "PNP": AtomicCube(1, -1, 1), "PPN": AtomicCube(1, 1, -1), "PPP": AtomicCube(1, 1, 1)}

cubes_init = {"000": AtomicCube(0, 0, 0), "NNN": AtomicCube(-1, -1, -1), "NNP": AtomicCube(-1, -1, 1),
              "NPN": AtomicCube(-1, 1, -1), "NPP": AtomicCube(-1, 1, 1), "PNN": AtomicCube(1, -1, -1),
              "PNP": AtomicCube(1, -1, 1), "PPN": AtomicCube(1, 1, -1), "PPP": AtomicCube(1, 1, 1)}


def printout(cubes):
    for (corner, cube) in cubes.items():
        print(corner + " " + str(cube))


def test(cubes):
    assert str(cubes["000"]) == "------"
    assert str(cubes["NNN"]) == "-x-y-z"
    assert str(cubes["NNP"]) == "-x-yZ-"
    assert str(cubes["NPN"]) == "-xY--z"
    assert str(cubes["NPP"]) == "-xY-Z-"
    assert str(cubes["PNN"]) == "X--y-z"
    assert str(cubes["PNP"]) == "X--yZ-"
    assert str(cubes["PPN"]) == "X-Y--z"
    assert str(cubes["PPP"]) == "X-Y-Z-"


def rotate(cubes, axis):
    for corner in cubes.keys():
        cubes[corner].rotate(axis)


# just print everything
# printout(cubes)

test(cubes)

cubes["PPP"].rotate(POS_Z)
assert str(cubes["PPP"]) == "Y--XZ-"

cubes["PPP"].rotate(POS_Z)
assert str(cubes["PPP"]) == "-X-YZ-"

cubes["PPP"].rotate(POS_Z)
assert str(cubes["PPP"]) == "-YX-Z-"

cubes["PPP"].rotate(POS_Z)
test(cubes)

# any 2 rotations 3 times takes the cube back to its original position.

for _ in range(3):
    rotate(cubes, POS_X)
    rotate(cubes, NEG_Y)
test(cubes)

for _ in range(3):
    rotate(cubes, POS_Y)
    rotate(cubes, POS_Z)
test(cubes)

for _ in range(3):
    rotate(cubes, NEG_Z)
    rotate(cubes, NEG_X)
test(cubes)

# 4 rotations about the same axis should take the cube to its starting point

for axis in AtomicCube.AXES:
    for corner in cubes.keys():
        #print(str(axis) + " " + corner + " " + str(cubes[corner]))
        for _ in range(4):
            cubes[corner].rotate(axis)
            #print(cubes[corner])
        test(cubes)
