from turtle import Turtle

MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
STARTING_POSITION = (0, -270)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def up(self):
        self.forward(MOVE_DISTANCE)
