
import CompositeCube as CC

STORE = {}

def lookupPuzzle(name):
    frozen = STORE[name]
    return thaw(frozen)
# END

def storePuzzle(name, cube):
    STORE[name] = freeze(cube)
# END

def thaw(frozen):
    pass
# END

def freeze(cube):
    pass
# END

def web_get(name, axis, ndx):

    cube = lookupPuzzle(name)

    cube.rotate(axis, ndx)

    web_respond(cube)

    storePuzzle(cube)
# END

def web_respond(cube):
    pass
# END
