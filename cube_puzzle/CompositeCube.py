from cube_puzzle.Vector3 import Vector3 as Vector3
from cube_puzzle.Vector3 import POS_X as POS_X
from cube_puzzle.Vector3 import POS_Y as POS_Y
from cube_puzzle.Vector3 import POS_Z as POS_Z
from cube_puzzle.Vector3 import NEG_X as NEG_X
from cube_puzzle.Vector3 import NEG_Y as NEG_Y
from cube_puzzle.Vector3 import NEG_Z as NEG_Z
from cube_puzzle.Vector3 import ZERO as ZERO
from cube_puzzle.AtomicCube import AtomicCube as AtomicCube


class CompositeCube:

    def __init__(self):

        # assign atomic cubes to 3D array. however the ordinates passed in are based on the cube being centered at the
        # origin, whereas the atoms array is indexed from zero.
        self.atoms = []
        for x in range(3):
            self.atoms.append([])
            for y in range(3):
                self.atoms[x].append([])
                for z in range(3):
                    self.atoms[x][y].append(AtomicCube(x-1, y-1, z-1))

    def rotate(self, axis: "Vector3", ndx: int):
        """
        axis: axis of rotation
        ndx: index will be -1, 0, 1 in direction of positive axis.
        """

        # these loops rotate the atomic cubes in place. this will effect one plane of the cube only.
        # iterate through every atomic cube.
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    # rotate atomic cubes in place, if they are in the specified index.
                    if (axis == POS_X or axis == NEG_X) and x - 1 == ndx:
                        self.atoms[x][y][z][0].rotate(axis)
                    elif (axis == POS_Y or axis == NEG_Y) and y - 1 == ndx:
                        self.atoms[x][y][z][0].rotate(axis)
                    elif (axis == POS_Z or axis == NEG_Z) and z - 1 == ndx:
                        self.atoms[x][y][z][0].rotate(axis)

        # these loops rotate the atomic cubes within the composite cube. this will effect one plane of the cube only.
        # iterate through every atomic cube.
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    # center cube remains in the same position always.
                    if x == 0 and y == 0 and z == 0:
                        continue
                    if (axis == POS_X or axis == NEG_X) and x - 1 == ndx:
                        self._move_cube(x, y, z, axis)
                    elif (axis == POS_Y or axis == NEG_Y) and y - 1 == ndx:
                        self._move_cube(x, y, z, axis)
                    elif (axis == POS_Z or axis == NEG_Z) and z - 1 == ndx:
                        self._move_cube(x, y, z, axis)

    def _move_cube(self, x: int, y: int, z: int, axis: "Vector3"):
        """
        moves an atomic cube to a new position within the composite cube.
        """
        atomic_cube = self.atoms[x][y][z][0]
        del self.atoms[x][y][z][0]
        # array indices start at zero but math is easier if the cube is centered in the origin.
        q = Vector3(x - 1, y - 1, z - 1).cross(axis)
        self.atoms[q.x + 1][q.y + 1][q.z + 1].append(atomic_cube)

    def flatten(self):
        """
        flatten the data into six two-dimensional arrays showing only the exposed faces of
         the atomic cubes.

        positive faces fold into Z plane facing positive
        where +X face meets +Z face rotate into Z plane, folding to the right from front edge
        where +Y face meets +Z face rotate into Z plane, folding up from the front edge
        +Z face is already in the Z plane

        negative faces fold into Z plane facing negative
        where -X face meets -Z face rotate into Z plane, folding to the left, from the back edge
        where -Y face meets -Z face rotate into Z plane, folding down, from the back edge
        -Z face is already in the Z plane
        """

        flat = {
            POS_X: [],
            POS_Y: [],
            POS_Z: [],
            NEG_X: [],
            NEG_Y: [],
            NEG_Z: []
        }

        # dimension the flat array
        for face_normal in flat.keys():
            for i in range(3):
                flat[face_normal].append([])
                for j in range(3):
                    flat[face_normal][i].append([])

        for face_normal in flat.keys():
            for h in range(3):
                for v in range(3):
                    # for [H][V] with H going left and V going down ...
                    #    +X H = -Z, V = -Y
                    #    +Y H = +X, V = +Z
                    #    +Z H = +X, V = -Y
                    #    -X H = -Z, V = -Y
                    #    -Y H = +X, V = +Z
                    #    -Z H = +X, V = -Y
                    if face_normal == POS_X:
                        flat[face_normal][h][v] = self.atoms[2][2-v][2-h].color(face_normal)
                    elif face_normal == POS_Y:
                        flat[face_normal][h][v] = self.atoms[h][2][v].color(face_normal)
                    elif face_normal == POS_Z:
                        flat[face_normal][h][v] = self.atoms[h][2-v][2].color(face_normal)
                    elif face_normal == NEG_X:
                        flat[face_normal][h][v] = self.atoms[0][2-v][2-h].color(face_normal)
                    elif face_normal == NEG_Y:
                        flat[face_normal][h][v] = self.atoms[h][0][v].color(face_normal)
                    elif face_normal == NEG_Z:
                        flat[face_normal][h][v] = self.atoms[h][2-v][0].color(face_normal)

        return flat


def print_flat_data(flat):
    """
    print faces of cube. the positive faces are folded onto the screen, then the cube is flipped to view -Z and the
    negative faces are folded onto the screen.
    """

    for y in range(3):

        print(" ", end=" ")
        face = flat[NEG_Z]
        for x in range(3):
            print(face[x][y], end="")

        print(" ", end=" ")
        face = flat[NEG_X]
        for x in range(3):
            print(face[x][y], end="")

        print(" ", end=" ")
        face = flat[POS_Y]
        for x in range(3):
            print(face[x][y], end="")

        print(" ", end=" ")
        for _ in range(3):
            print(" ", end="")

        print("")
    print("")

    for y in range(3):

        print(" ", end=" ")
        face = flat[NEG_Y]
        for x in range(3):
            print(face[x][y], end="")

        print(" ", end=" ")
        for _ in range(3):
            print(" ", end="")

        print(" ", end=" ")
        face = flat[POS_Z]
        for x in range(3):
            print(face[x][y], end="")

        print(" ", end=" ")
        face = flat[POS_X]
        for x in range(3):
            print(face[x][y], end="")

        print("")
    print("")

    # END


cube = CompositeCube()
flat = cube.flatten()
print_flat_data(flat)
