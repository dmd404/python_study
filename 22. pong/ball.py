from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(5)
        self.color('white')
        self.shape('circle')

    def move(self):
        self.setheading(38)
        self.forward(5)
