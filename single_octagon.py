import numpy
from math import *

def intOf(floatVal):
    return int(round(floatVal))

i = 90

xl = i * cos(pi / 8)
yl = i * sin(pi / 8)
xh = i * cos(3 * pi / 8)
yh = i * sin(3 * pi / 8)
print "1st quadrant", xl, yl, xh, yh    

#new origin
org = -xl

#<a xlink:href="#"><polygon class="teal" points="0 0 80 0 40 40" /></a>
    
#print "Iteration", i
print xl - org, yl - org
print xh - org, yh - org
print -xh - org, yh - org
print -xl - org, yl - org
print -xl - org, -yl - org
print -xh - org, -yh - org
print xh - org, intOf(-yh - org)
print xl - org, -yl - org

print intOf(xl - org), intOf(yl - org), intOf(xh - org), intOf(yh - org), intOf(-xh - org), intOf(yh - org), intOf(-xl - org), intOf(yl - org), intOf(-xl - org), intOf(-yl - org), intOf(-xh - org), intOf(-yh - org), intOf(xh - org), intOf(-yh - org), intOf(xl - org), intOf(-yl - org)

#all the vertices of the i'th hexagon (after translation to new origin)
#x[j][0], y[j][0] = x30 - ox, y30 - oy
#print x[j][0], y[j][0]
#x[j][1], y[j][1] = x30 - ox, -y30 - oy
#print x[j][1], y[j][1]
#x[j][2], y[j][2] = -x30 - ox, y30 - oy
#x[j][3], y[j][3] = -x30 - ox, -y30 - oy
#x[j][4], y[j][4] = x60 - ox, y60 - oy
#x[j][5], y[j][5] = x60 - ox, -y60 - oy
#x[j][6], y[j][6] = -x60 - ox, y60 - oy
#x[j][7], y[j][7] = -x60 - ox, -y60 - oy
