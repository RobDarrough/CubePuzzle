import Z3 as Z3
import AtomicCube as AC


class CompositeCube:

    def __init__(self, name):

        # the name should be a unique 3 character string. characters must be ASCII.
        self.name = name

        # since the name is unique it can be used for the hash code. there are 128 ASCII codes.
        self.hashcode = 16384 * ord(name[0]) + 128 * ord(name[1]) + ord(name[2])

        self.atoms = []
        for x in range(3):
            self.atoms.append([])
            for y in range(3):
                self.atoms[x].append([])
                for z in range(3):
                    name = str(x) + str(y) + str(z)
                    self.atoms[x][y].append(AC.AtomicCube(name))
    # END

    def __str__(self):
        return self.name
    # END

    def __eq__(self, p):
        return self.name == p.name
    # END

    def __hash__(self):
        return self.hashcode
    # END

    def rotate(self, axis, ndx):
        pass
    # END

    def flatten(self):
        """
        flatten the data into six two-dimensional arrays showing only the exposed faces of the atomic cubes.

        positive faces fold into Z plane facing positive
        where +X face meets +Z face rotate into Z plane, folding to the right from front edge
        where +Y face meets +Z face rotate into Z plane, folding up from the front edge
        +Z face is already in the Z plane

        negative faces fold into Z plane facing negative
        where -X face meets -Z face rotate into Z plane, folding to the left, from the back edge
        where -Y face meets -Z face rotate into Z plane, folding down, from the back edge
        -Z face is already in the Z plane

        for [H][V] with H going left and V going down ...
        +X H = -Z, V = -Y
        +Y H = +X, V = +Z
        +Z H = +X, V = -Y
        -X H = -Z, V = -Y
        -Y H = +X, V = +Z
        -Z H = +X, V = -Y
        """

        flat = {
            Z3.POS_X: [],
            Z3.POS_Y: [],
            Z3.POS_Z: [],
            Z3.NEG_X: [],
            Z3.NEG_Y: [],
            Z3.NEG_Z: []
        }

        for key in flat.keys():
            for h in range(3):
                flat[key].append([])
                for v in range(3):
                    if key == Z3.POS_X:
                        flat[key][h] = self.atoms[2][3-v][3-h].color(key)
                    elif key == Z3.POS_Y:
                        flat[key][h] = self.atoms[h][2][v].color(key)
                    elif key == Z3.POS_Z:
                        flat[key][h] = self.atoms[h][3-v][2].color(key)
                    elif key == Z3.NEG_X:
                        flat[key][h] = self.atoms[0][3-v][3-h].color(key)
                    elif key == Z3.NEG_Y:
                        flat[key][h] = self.atoms[h][0][v].color(key)
                    elif key == Z3.NEG_Z:
                        flat[key][h] = self.atoms[h][3-v][0].color(key)
    # END