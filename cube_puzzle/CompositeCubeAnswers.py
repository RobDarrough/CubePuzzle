import Z3 as Z3

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
    match code:
        case "+X":
            return Z3.POS_X
        case "+Y":
            return Z3.POS_Y
        case "+Z":
            return Z3.POS_Z
        case "-X":
            return Z3.NEG_X
        case "-Y":
            return Z3.NEG_Y
        case "-Z":
            return Z3.NEG_Z
    return None


def AxisToCode(axis):
    match axis:
        case Z3.POS_X:
            return "+X"
        case Z3.POS_Y:
            return "+Y"
        case Z3.POS_Z:
            return "+Z"
        case Z3.NEG_X:
            return "-X"
        case Z3.NEG_Y:
            return "-Y"
        case Z3.NEG_Z:
            return "-Z"
    return None


answers = ReadAnswersFile()
ShowAnswers(answers)
