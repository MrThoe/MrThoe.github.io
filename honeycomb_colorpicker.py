import turtle as t
from random import randint


r = 255
g = 255
b = 255

def hexagon(r, g, b):
    sven.color(r,g,b)

    sven.begin_fill()
    for i in range(6):
        sven.forward(20)
        sven.right(60)
    sven.end_fill()
    
def move(n):
    for i in range (n):
        sven.forward(20)
        sven.right(60)

    sven.left(n*60)

sven=t.Turtle()
sven.speed(0)
wn=t.Screen()
wn.colormode(255)
wn.bgcolor(0,0,0)

hexagon(r, g, b)           #Beginning
set()

def set():
    sven.left(120)      #Set piece on top to begin next round
    move(2)
    sven.right(120)

def top_right():
    hexagon(r, g, b)           #Top + Top right side
    move(2)

def right():
    hexagon(r, g, b)
    move(4)             #Right side

def bottom_right():
    hexagon(r, g, b)
    sven.right(120)     #Bottom
    move(2)
    sven.left(120)

def bottom_left():    
    hexagon(r, g, b)
    sven.right(120)     #Bottom Left
    move(4)
    sven.left(120)

def left():
    hexagon(r, g, b)
    sven.left(120)      #left
    move(2)
    sven.right(120)


def top_left():
    hexagon(r, g, b)
    sven.forward(20)
    sven.left(60)
    sven.forward(20)
    sven.right(60)

def reset():
    sven.left(120)      #Set piece on top to begin next round
    move(2)
    sven.right(120)

for n in range(1,7):
    set()
    r = 255
    g = 255
    b = 255

    for i in range (n):        
        if r > 50:
            r = r - 51
        top_right()
    for i in range (n):
        if g > 50:
            g = g - 51
        right()
    for i in range (n):
        if r < 205:
            r = r + 51
        bottom_right()
    for i in range (n):
        if b > 50:
            b = b - 51
        bottom_left()
    for i in range (n):
        if g <205:
            g = g + 51
        left()
    for i in range (n):
        if r > 50:
            r = r - 51
        top_left()
