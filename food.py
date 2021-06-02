from turtle import Turtle
import random as r

# create a class for the food, changing it's appearance to that of a small white dot displayed at a random coordinate
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('white')
        self.speed('fastest')
        self.refresh()
        
    # send the food to a new random coordinate
    def refresh(self):
        rand_x = r.randint(-280, 280)
        rand_y = r.randint(-280, 280)
        self.goto(rand_x, rand_y)
