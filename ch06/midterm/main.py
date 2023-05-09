import turtle
import random 

t = turtle.Turtle()

main_angle = 90
special_angle = 45

def random_color(): 
    colors = ["Pink", "purple", "lightgreen", "blue"]
    return random.choice(colors)

def base(length):
    t.begin_fill()
    t.color(random_color())
    t.forward(length)
    t.right(main_angle)
    t.forward(length)
    t.right(main_angle)
    t.forward(length)
    t.right(main_angle)
    t.forward(length)
    t.end_fill()
    return length

def roof(length):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.begin_fill()
    t.color(random_color())
    t.right(special_angle)
    t.forward(107)
    t.right(main_angle)
    t.forward(107)
    t.end_fill()
    return length 

def door(length):
    t.penup()
    t.goto(75, -90)
    t.pendown()
    t.begin_fill()
    t.color("Red", "white")
    t.right(special_angle)
    t.forward(60)
    t.right(main_angle)
    t.forward(40)
    t.right(main_angle)
    t.forward(60)
    t.right(main_angle)
    t.forward(40)
    t.end_fill()

    t.penup()
    t.goto(115, -90)
    t.pendown()
    t.begin_fill()
    t.color("Red", "white")
    t.right(main_angle)
    t.forward(60)
    t.right(main_angle)
    t.forward(40)
    t.right(main_angle)
    t.forward(60)
    t.right(main_angle)
    t.forward(40)
    t.end_fill()

def window(length):
    t.penup()
    t.goto(20, -20)
    t.color("white", "purple")
    t.pendown()
    t.begin_fill()
    t.forward(40)
    t.right(main_angle)
    t.forward(50)
    t.right(main_angle)
    t.forward(40)
    t.right(main_angle)
    t.forward(50)
    t.end_fill()
    
    t.penup()
    t.goto(90, -70)
    t.color("white", "purple")
    t.pendown()
    t.begin_fill()
    t.forward(50)
    t.right(main_angle)
    t.forward(40)
    t.right(main_angle)
    t.forward(50)
    t.right(main_angle)
    t.forward(40)
    t.end_fill()
   
def chimney(length):
    t.penup()
    t.goto(120, 20)
    t.pendown()
    t.begin_fill()
    t.color(random_color())
    t.forward(20)
    t.right(main_angle)
    t.forward(20)
    t.right(main_angle)
    t.forward(20)
    t.right(main_angle)
    t.forward(20)
    t.right(main_angle)
    t.end_fill()
    return length 

def main():
    base(150)
    roof(150)
    door(150)
    window(150)
    chimney(150)
    t.end_fill

main ()
t.hideturtle()
turtle.done()