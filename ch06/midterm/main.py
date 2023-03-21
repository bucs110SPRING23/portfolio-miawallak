import turtle

t = turtle.Turtle()

special_angle = 45

# Draw the main house structure
def base(length):
    t.begin_fill()
    t.color("Pink")
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.end_fill()
    roof(length)
    
def roof(length):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.begin_fill()
    t.color("green")
    t.right(special_angle)
    t.forward(107)
    t.right(90)
    t.forward(107)
    t.end_fill()
    door(length)

def door(length):
    t.penup()
    t.goto(75, -90)
    t.pendown()
    t.begin_fill()
    t.color("Red", "white")
    t.right(special_angle)
    t.forward(60)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(40)
    t.end_fill()

    t.penup()
    t.goto(115, -90)
    t.pendown()
    t.begin_fill()
    t.color("Red", "white")
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(40)
    t.end_fill()
    window(length)

def window(length):
    # Draw the windows of the house
    t.penup()
    t.goto(20, -20)
    t.color("white", "purple")
    t.pendown()
    t.begin_fill()
    t.forward(40)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(50)
    t.end_fill()
    
    t.penup()
    t.goto(90, -70)
    t.color("white", "purple")
    t.pendown()
    t.begin_fill()
    t.forward(50)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(40)
    t.end_fill()
    chimney(length)
   
# Draw the chimney
def chimney(length):
    t.penup()
    t.goto(120, 20)
    t.pendown()
    t.begin_fill()
    t.color("lightgreen")
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.end_fill()

base(150)
t.end_fill

# Hide the turtle
t.hideturtle()

# Keep the window open until closed manually
turtle.done()

