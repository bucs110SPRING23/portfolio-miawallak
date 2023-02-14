import turtle #1. import modules
import random

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
michelangelo.forward(random.randrange(1, 100))
leonardo.forward(random.randrange(1,100))
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)




for i in range(10):
    michelangelo.forward(random.randrange(1,10))
    leonardo.forward(random.randrange(1,10))

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
window.exitonclick()


# PART B - complete part B here
import pygame
import math

pygame.init()
window = pygame.display.set_mode((500, 500))

points = []
sides = [3, 4, 6, 20, 100, 360]
side_length = 100
xpos = 250
ypos = 250

for num_sides in sides:
    points = []
    window.fill("black")
    for i in range(num_sides):
        angle = 360/num_sides
        radians = math.radians(angle * i)
        x = xpos + side_length * math.cos(radians)
        y = ypos + side_length * math.sin(radians)
        points.append((x,y))
    pygame.draw.polygon(window, (0, 0, 255), points)
    pygame.display.flip()
    pygame.time.wait(3000)

pygame.quit()