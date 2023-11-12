from cube_puzzle.Vector3 import Vector3 as Vector3
from cube_puzzle.Vector3 import POS_X as POS_X
from cube_puzzle.Vector3 import POS_Y as POS_Y
from cube_puzzle.Vector3 import POS_Z as POS_Z
from cube_puzzle.Vector3 import NEG_X as NEG_X
from cube_puzzle.Vector3 import NEG_Y as NEG_Y
from cube_puzzle.Vector3 import NEG_Z as NEG_Z
from cube_puzzle.Vector3 import ZERO as ZERO
from cube_puzzle.AtomicCube import AtomicCube as AtomicCube


def ReadAnswersFile():
    '''
    reads in the answers for a series of tests for the CompositeCube class.
    '''

    f = open("CompositeCubeAnswers.dat", "r")
    lines = f.readlines()
    f.close()

    answers = {}
    axis = None
    ndx = None

    # iterate the lines
    for (row, line) in enumerate(lines):

        # skip blank lines
        if line.strip() == "":
            continue

        # short lines are axis and index for the answer
        if len(line) < 15:
            (code, ndx) = line.split()
            axis = CodeToAxis(code)

            # create nested dictionaries to hold the answer

            if axis not in answers:
                answers[axis] = {}

            if ndx not in answers[axis]:
                answers[axis][ndx] = {}

            continue

        # invariant: line is at least 15 chars
        # long lines are a sequence of characters, each one specifying the color of a face.
        for c in line.strip():
            # blanks separate faces for human readability, skip them
            if c == ' ':
                continue
            else:
                if row not in answers[axis][ndx]:
                    answers[axis][ndx][row] = []

                answers[axis][ndx][row].append(c)

    return answers


def ShowAnswers(answers):
    '''
    print human readable form of answers on to console.
    '''

    # {axis : {ndx : {row : [col]}}}

    for axis in answers.keys():
        for ndx in answers[axis].keys():
            print(f"{AxisToCode(axis)} {ndx}")
            for row in answers[axis][ndx].keys():
                for (col, c) in enumerate(answers[axis][ndx][row]):
                    # every third column add a row of blanks
                    if col % 3 == 2:
                        print(f"{c} ", end="")
                    else:
                        print(c, end="")
                print("")


def CodeToAxis(code):

    if code == "+X":
        return POS_X
    elif code == "+Y":
        return POS_Y
    elif code == "+Z":
        return POS_Z
    elif code == "-X":
        return NEG_X
    elif code == "-Y":
        return NEG_Y
    elif code == "-Z":
        return NEG_Z

    return None


def AxisToCode(axis):

    if axis == POS_X:
        return "+X"
    elif axis == POS_Y:
        return "+Y"
    elif axis == POS_Z:
        return "+Z"
    elif axis == NEG_X:
        return "-X"
    elif axis == NEG_Y:
        return "-Y"
    elif axis == NEG_Z:
        return "-Z"

    return None


answers = ReadAnswersFile()
ShowAnswers(answers)
