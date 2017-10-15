import numpy
from math import *

def intOf(floatVal):
    return int(round(floatVal))

i = 90

x30 = i * cos(pi / 8)
y30 = i * sin(pi / 8)
x60 = i * cos(3 * pi / 8)
y60 = i * sin(3 * pi / 8)
print "1st quadrant", x30, y30, x60, y60    

print "test", cos(pi/16), sin(3 * pi / 16)
#new origin
org = -x30

#<a xlink:href="#"><polygon class="teal" points="0 0 80 0 40 40" /></a>
    
#print "Iteration", i
print x30 - org, y30 - org
print x60 - org, y60 - org
print -x60 - org, y60 - org
print -x30 - org, y30 - org
print -x30 - org, -y30 - org
print -x60 - org, -y60 - org
print x60 - org, intOf(-y60 - org)
print x30 - org, -y30 - org

print intOf(x30 - org), intOf(y30 - org), intOf(x60 - org), intOf(y60 - org), intOf(-x60 - org), intOf(y60 - org), intOf(-x30 - org), intOf(y30 - org), intOf(-x30 - org), intOf(-y30 - org), intOf(-x60 - org), intOf(-y60 - org), intOf(x60 - org), intOf(-y60 - org), intOf(x30 - org), intOf(-y30 - org)

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
