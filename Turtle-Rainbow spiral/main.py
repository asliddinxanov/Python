import turtle
from turtle import *
turtle.setup(1000, 1000, 0, 0)
turtle.bgcolor('black')
turtle.speed(0)

r, g, b = 255, 0, 0

for i in range(255*2):
    colormode(255)
    if i < 255//3:
        g += 2
    elif i < 255*2//3:
        r -= 2
    elif i < 255:
        b += 2
    elif i < 255*4//3:
        g -= 2
    elif i < 255*5//3:
        r += 2
    else:
        b -= 20
    fd(50+i)
    rt(111)
    pencolor(r, g, b)
