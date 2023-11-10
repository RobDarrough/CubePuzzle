import Z3 as Z3


class AtomicCube:

    # this is the default ordering of the axes. it is used in the string representation.
    AXES = (Z3.POS_X, Z3.NEG_X, Z3.POS_Y, Z3.NEG_Y, Z3.POS_Z, Z3.NEG_Z)

    AXISNAMES = {Z3.POS_X : "X", Z3.NEG_X : "x",
                 Z3.POS_Y : "Y", Z3.NEG_Y : "y",
                 Z3.POS_Z : "Z", Z3.NEG_Z : "z"}

    COLORS =    {Z3.POS_X : "R", Z3.NEG_X : "B",
                 Z3.POS_Y : "O", Z3.NEG_Y : "P",
                 Z3.POS_Z : "Y", Z3.NEG_Z : "G"}

    # with debug the string representation will use AXISNAMES instead of COLORS.
    DEBUG = False

    def __init__(self, name):

        # the name is a 3 character string that indicates the position of the
        # cube within a composite cube. characters must be ASCII.
        self.name = name

        # since the position of the cube with the composite cube is unique it
        # can be used for the hash code. there are 128 ASCII codes.
        self.hashcode = 16384 * ord(name[0]) + 128 * ord(name[1]) + ord(name[2])

        self.faces = {}
        if AtomicCube.DEBUG:
            for axis in AtomicCube.AXES:
                self.faces[axis] = [AtomicCube.AXISNAMES[axis] + name]
        else:
            for axis in AtomicCube.AXES:
                self.faces[axis] = [AtomicCube.COLORS[axis]]
    # END

    def __str__(self):
        s = self.name + "("
        for axis in AtomicCube.AXES:
            s += self.faces[axis][0]
        s = self.name + ")"
        return s
    # END

    def __eq__(self, p):
        return self.name == p.name
    # END

    def __hash__(self):
        return self.hashcode
    # END

    def rotate(self, axis):
        """
        clockwise quarter turn around the specified axis
        """
        # invariant: the array corresponding to each face is size one.
        for axis0 in AtomicCube.AXES:
            if len(self.faces[axis0]) != 1:
                assert True

        for axis0 in AtomicCube.AXES:
            # cross product of colinear vectors is zero
            if axis.cross(axis0) != Z3.ZERO:
                face = self.faces[axis0][0]
                del self.faces[axis0][0]
                # re-assign the face to the rotated position
                # A X B is clockwise quarter turn of A around B
                newaxis = axis0.cross(axis)
                # if newaxis has already been processed then append assigns to [0]
                # otherwise it assigns to [1] and that becomes [0] when the newaxis is processed.
                self.faces[newaxis].append(face)

        # invariant: the array corresponding to each face is size one.
        for axis0 in AtomicCube.AXES:
            if len(self.faces[axis0]) != 1:
                assert True

    # END

    def color(self, axis):
        """
        returns the color of the specified face
        """
        return self.faces[axis][0]
    # END