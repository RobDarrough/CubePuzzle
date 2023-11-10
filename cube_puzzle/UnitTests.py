
import Z3 as Z3
import AtomicCube as AC

p = Z3.POS_X + Z3.POS_Y + Z3.POS_Z
print("(1, 1, 1) " + str(p))

q = Z3.POS_X + Z3.POS_Z
print("(1, 0, 1) " + str(q))

r = p - q
print("(0, 1, 0) " + str(r))

print("True " + str(r == Z3.POS_Y))

# repeat with negative unit vectors
p = Z3.NEG_X + Z3.NEG_Y + Z3.NEG_Z
print("(-1, -1, -1) " + str(p))

q = Z3.NEG_X + Z3.NEG_Z
print("(-1, 0, -1) " + str(q))

r = p - q
print("(0, -1, 0) " + str(r))

print("True " + str(r == Z3.NEG_Y))

p = Z3.POS_X.scale(3) + Z3.POS_Y.scale(4) + Z3.POS_Z.scale(5)
print("(3, 4, 5) " + str(p))
print("True " + str(p == Z3.Z3(3, 4, 5)))

Z = Z3.POS_X.cross(Z3.POS_Y)
print("(0, 0, 1) " + str(Z))
print("True " + str(Z == Z3.POS_Z))

X = Z3.POS_Y.cross(Z3.POS_Z)
print("(1, 0, 0) " + str(X))
print("True " + str(X == Z3.POS_X))

Y = Z3.POS_Z.cross(Z3.POS_X)
print("(0, 1, 0) " + str(Y))
print("True " + str(Y == Z3.POS_Y))

Z = Z3.NEG_Y.cross(Z3.NEG_X)
print("(0, 0, -1) " + str(Z))
print("True " + str(Z == Z3.NEG_Z))

X = Z3.NEG_Z.cross(Z3.NEG_Y)
print("(-1, 0, 0) " + str(X))
print("True " + str(X == Z3.NEG_X))

Y = Z3.NEG_X.cross(Z3.NEG_Z)
print("(0, -1, 0) " + str(Y))
print("True " + str(Y == Z3.NEG_Y))

AC.AtomicCube.DEBUG = False

acube0 = AC.AtomicCube("+++")
print("X+++ R " + str(acube0.color(Z3.POS_X)))
print("Y+++ O " + str(acube0.color(Z3.POS_Y)))
print("Z+++ Y " + str(acube0.color(Z3.POS_Z)))
print("x+++ B " + str(acube0.color(Z3.NEG_X)))
print("y+++ P " + str(acube0.color(Z3.NEG_Y)))
print("z+++ G " + str(acube0.color(Z3.NEG_Z)))

print("X+++x+++Y+++y+++Z+++z+++ RBOPYG " + str(acube0))

acube0.rotate(Z3.POS_Z)
print("Y+++y+++x+++X+++Z+++z+++ OPBRYG " + str(acube0))

acube0.rotate(Z3.NEG_Z)
print("X+++x+++Y+++y+++Z+++z+++ RBOPYG " + str(acube0))

# any two perpendicular axes 3 times should be back to the starting point.

for _ in range(3):
    acube0.rotate(Z3.POS_X)
    acube0.rotate(Z3.POS_Y)
print("X+++x+++Y+++y+++Z+++z+++ RBOPYG " + str(acube0))

for _ in range(3):
    acube0.rotate(Z3.POS_Z)
    acube0.rotate(Z3.NEG_X)
print("X+++x+++Y+++y+++Z+++z+++ RBOPYG " + str(acube0))

for _ in range(3):
    acube0.rotate(Z3.NEG_Y)
    acube0.rotate(Z3.NEG_Z)
print("X+++x+++Y+++y+++Z+++z+++ RBOPYG " + str(acube0))
