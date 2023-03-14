import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(width=500, height=500)
turtle = turtle.Turtle()


turtle.penup()
turtle.goto(0,0)
turtle.pendown()

def off_screen(turtle):
    x,y = turtle.position()
    if abs(x) > 250 or abs(y) > 250:
        return True
    else:
        return False

while not off_screen(turtle):
    if random.randint(0, 1) == 0:
        turtle.left(90)
    else:
        turtle.right(90)

    for i in range(50):
        turtle.forward(5)

    if off_screen(turtle):
        break

turtle.done()