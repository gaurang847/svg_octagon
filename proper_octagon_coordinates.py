from math import *
import numpy

side = 121
n = 8
nLevels = 11
org = - side * cos(pi / 8) - 80
#print nLevels
x, y = numpy.zeros((nLevels, n)), numpy.zeros((nLevels, n))
j = 0

def intOf(floatVal):
    return int(round(floatVal))


for i in range(side/nLevels, side + 1, side/nLevels):
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

i = 7
while i > 0:
    for j in range(nLevels - 1):
        tx1 = x[j][i]
        tx4 = x[j][i - 1]
        tx2 = x[j+1][i]
        tx3 = x[j+1][i-1]
        ty1 = y[j][i]
        ty4 = y[j][i - 1]
        ty2 = y[j+1][i]
        ty3 = y[j+1][i-1]
        print '<a xlink:href="#"><polygon id = "segment' + str(i) + str(j) + '" onclick="colorChange(\'segment' + str(i) + str(j) + '\')" class="slice-' + str(i) + '" points="', tx1, ty1, tx2, ty2, tx3, ty3, tx4, ty4, '" /></a>'

        
    i-=1

for j in range(nLevels - 1):
    tx1 = x[j][0]
    tx4 = x[j][7]
    tx2 = x[j+1][0]
    tx3 = x[j+1][7]
    ty1 = y[j][0]
    ty4 = y[j][7]
    ty2 = y[j+1][0]
    ty3 = y[j+1][7]
    print '<a xlink:href="#"><polygon id = "segment' + str(0) + str(j) + '" onclick="colorChange(\'segment' + str(0) + str(j) + '\')" class="slice-0" points="', tx1, ty1, tx2, ty2, tx3, ty3, tx4, ty4, '" /></a>'

line = '<polyline points="'
for i in xrange(8):
    if i != 0:
        line = line + " "
    line = line + str(x[0][i]) + " " + str(y[0][i])
line = line + " " + str(x[0][0]) + " " + str(y[0][0])
line = line + '" />'
print line

line = '<polyline points="'
for i in xrange(8):
    if i != 0:
        line = line + " "
    line = line + str(x[10][i]) + " " + str(y[10][i])
line = line + " " + str(x[10][0]) + " " + str(y[10][0])
line = line  + '" />'
print line

#x[level][slice]
for i in xrange(8):
    print '<line x1="' + str(x[0][i]) + '" y1="' + str(y[0][i]) + '" x2="' + str(x[10][i]) + '" y2="' + str(y[10][i]) + '" />'
