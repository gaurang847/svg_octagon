from math import *
import numpy

sides = 90
n = 8
nLevels = sides / (n + 1)
org = - sides * cos(pi / 8)
print nLevels
x, y = numpy.zeros((sides, n)), numpy.zeros((sides, n))
j = 0

def intOf(floatVal):
    return int(round(floatVal))


for i in range(sides/(n + 1), sides + 1, sides/(n + 1)):
    #print "i value", i
    #two points in one quadrant of an octagon
    xl = i * cos(pi / 8)
    yl = i * sin(pi / 8)
    xh = i * cos(3 * pi / 8)
    yh = i * sin(3 * pi / 8)
    #print "1st quadrant", xl, yl, xh, yh    

    #new origin
    #org = -xl

    #<a xlink:href="#"><polygon class="teal" points="0 0 80 0 40 40" /></a>
    

    #all the vertices of the i'th hexagon (after translation to new origin)
    x[j][0], y[j][0] = xl - org, yl - org
    x[j][1], y[j][1] = xh - org, yh - org
    x[j][2], y[j][2] = -xh - org, yh - org
    x[j][3], y[j][3] = -xl - org, yl - org
    x[j][4], y[j][4] = -xl - org, -yl - org
    x[j][5], y[j][5] = -xh - org, -yh - org
    x[j][6], y[j][6] = xh - org, intOf(-yh - org)
    x[j][7], y[j][7] = xl - org, -yl - org

    print intOf(xl - org), intOf(yl - org), intOf(xh - org), intOf(yh - org), intOf(-xh - org), intOf(yh - org), intOf(-xl - org), intOf(yl - org), intOf(-xl - org), intOf(-yl - org), intOf(-xh - org), intOf(-yh - org), intOf(xh - org), intOf(-yh - org), intOf(xl - org), intOf(-yl - org)
    j+=1

for i in range(nLevels):
    for j in range(n - 1):
        tx1, ty1 = intOf(x[i][j]), intOf(y[i][j])
        tx2, ty2 = intOf(x[i][j + 1]), intOf(y[i][j + 1])
        tx3, ty3 = intOf(x[i + 1][j]), intOf(y[i + 1][j])
        tx4, ty4 = intOf(x[i + 1][j + 1]), intOf(y[i + 1][j + 1])
        #print '<a xlink:href="#"><polygon class="teal" points="', tx1, ty1, tx2, ty2, tx3, ty3, tx4, ty4, '" /></a>'
