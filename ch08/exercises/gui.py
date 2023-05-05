class Player:
    def __init__(self, name, height, shape):
        self.name = name
        self.height = height
        self.shape = shape

class Enemy:
    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed

class background:
    def __init__(self, trees, flowers, grass):
        self.trees = trees
        self.flowers = flowers
        self.grass = grass 