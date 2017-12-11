import turtle as t
from random import randint

sven = t.Turtle()
wn = t.Screen()
wn.colormode(255)
wn.bgcolor(0,0,0)

r = 255
g = 255
b = 255
sven.color(r,g,b)
sven.speed(4)
def rhombus(r,g,b, s):
    sven.color(r,g,b)
    sven.begin_fill()
    for i in range(2):
        sven.forward(s)
        sven.left(60)
        sven.forward(s)
        sven.left(120)
    sven.end_fill()

def cube(s, theta):
    sven.pu()
    sven.goto(0, -s)
    sven.pd()
    sven.setheading(theta)
    rhombus(237, 65,55, s)   
    sven.right(60)
    rhombus(54, 124, 248, s)
    sven.left(60)
    sven.forward(s)
    sven.right(60)
    sven.forward(s)
    sven.left(120)
    rhombus(247,184,1, s)
    sven.goto(0,0)
def cube2(s, theta):
    sven.pu()
    sven.goto(0, s)
    sven.pd()
    sven.setheading(-theta)
    rhombus(237, 65,55, s)
    sven.right(60)
    rhombus(54, 124, 248, s)
    sven.left(60)
    sven.forward(s)
    sven.right(60)
    sven.forward(s)
    sven.left(120)
    rhombus(247,184,1, s)
    sven.goto(0,0)

for i in range(2):
    cube(100 - 40*i, 90)
    cube2(80 - 40*i, 90)

cube(20, 90)
