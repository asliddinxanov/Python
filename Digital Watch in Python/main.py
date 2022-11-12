import time
import datetime as dt
import turtle
t = turtle.Turtle()
# create a turtle to create rectangle box
#t1 = turtle.Turtle()
# create screen
s = turtle.Screen()
turtle.setup(300, 300, 10, 10)
# set background color of the screen
#s.bgcolor("cyan")
# obtain current hour, minute and second
sec = dt.datetime.now().second
min_t = dt.datetime.now().minute
hr = dt.datetime.now().hour
#t1.pensize(10)
#t1.color('red')
#t1.penup()
# set the position of turtle
#t1.goto(-20, -0)
#t1.pendown()
# create rectangular box
'''for i in range(2):
    t1.forward(200)
    t1.left(90)
    t1.forward(70)
    t1.left(90)
    t1.hideturtle()'''

while True:
    t.hideturtle()
    t.clear()
# display the time
    t.write(str(hr).zfill(2) + ":" + str(min_t).zfill(2)+":"+str(sec).zfill(2), font=("Arial Narrow", 25, "bold"))
    time.sleep(1)
    sec += 1
    if sec == 60:
        sec = 0
        min_t += 1
    if min == 60:
        min_t = 0
        hr += 1
    if hr == 13:
        hr = 1