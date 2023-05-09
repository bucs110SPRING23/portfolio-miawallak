import turtle
t = turtle.Turtle()

sides = int(input("Enter number of sides "))
length = int(input("Enter length of sides "))
t.color('pink')
for i in range(sides):
    t.forward(length)
    t.right(90)
turtle.done()