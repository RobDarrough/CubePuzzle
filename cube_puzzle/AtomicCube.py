from cube_puzzle.Vector3 import Vector3 as Vector3
from cube_puzzle.Vector3 import POS_X as POS_X
from cube_puzzle.Vector3 import POS_Y as POS_Y
from cube_puzzle.Vector3 import POS_Z as POS_Z
from cube_puzzle.Vector3 import NEG_X as NEG_X
from cube_puzzle.Vector3 import NEG_Y as NEG_Y
from cube_puzzle.Vector3 import NEG_Z as NEG_Z
from cube_puzzle.Vector3 import ZERO as ZERO


class AtomicCube:

    # this is the default ordering of the axes. it is used in the string representation.
    AXES = (POS_X, NEG_X, POS_Y, NEG_Y, POS_Z, NEG_Z)

    # maps the various faces to initial colors. the vector is the normal to the face having the specified color.
    COLORS = {POS_X: "X", NEG_X: "x",
              POS_Y: "Y", NEG_Y: "y",
              POS_Z: "Z", NEG_Z: "z"}

    def __init__(self, x: int, y: int, z: int):
        """
        x, y, z: ordinates of this cube within the composite cube. use values -1, 0, 1
        """
        # since the initial position of the cube with the composite cube is unique it
        # can be used for the hash code. note that the hashcode does not change when
        # the cube is moved. the hash code is based upon the INITIAL position.
        self.hashcode = 100 * x + 10 * y + z

        # only provide values for faces that are exposed.
        self.faces = {}
        for axis in AtomicCube.AXES:
            if axis == POS_X:
                self._set_color(axis, x, 1)
            elif axis == POS_Y:
                self._set_color(axis, y, 1)
            elif axis == POS_Z:
                self._set_color(axis, z, 1)
            elif axis == NEG_X:
                self._set_color(axis, x, -1)
            elif axis == NEG_Y:
                self._set_color(axis, y, -1)
            elif axis == NEG_Z:
                self._set_color(axis, z, -1)

    def _set_color(self, axis: "Vector3", val: float, val0: float):
        """
        if axis == axis0 and val == val0 then this is an exterior face and so color it.
        """

        # note that every face is actually an array of colors. only the first entry matters. others are temporary.
        if val == val0:
            self.faces[axis] = [AtomicCube.COLORS[axis]]
        else:
            self.faces[axis] = ["-"]

    def __str__(self) -> str:
        s = ""
        for axis in AtomicCube.AXES:
            s += self.faces[axis][0]
        return s

    def __eq__(self, p: "AtomicCube") -> bool:
        return self.hashcode == p.hashcode

    def __hash__(self) -> int:
        return self.hashcode

    def rotate(self, axis: "Vector3"):
        """
        clockwise quarter turn around the specified axis
        """
        # invariant: the array corresponding to each face is size one.
        for axis0 in AtomicCube.AXES:
            if len(self.faces[axis0]) != 1:
                assert True

        for axis0 in AtomicCube.AXES:
            # cross product of co-linear vectors is zero
            if axis.cross(axis0) != ZERO:
                # copy and remove the face from the cube.
                face = self.faces[axis0][0]
                del self.faces[axis0][0]
                # re-assign the face to the rotated position
                # A X B is clockwise quarter turn of A around B
                q = axis0.cross(axis)
                # if q has already been processed then append assigns to [0]. otherwise it assigns to [1] and that
                # becomes [0] when the q is processed.
                self.faces[q].append(face)

        # invariant: the array corresponding to each face is size one.
        for axis0 in AtomicCube.AXES:
            if len(self.faces[axis0]) != 1:
                assert True

    def color(self, axis: "Vector3") -> str:
        """
        returns the color of the specified face
        """
        # note that every face is actually an array of colors. only the first entry matters. others are temporary.
        return self.faces[axis][0]
