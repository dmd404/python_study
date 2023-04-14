from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(5)
        self.color('white')
        self.shape('circle')
        self.x_move = 10
        self.y_move = 10

    def move(self, test):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1


        # self.setheading(38)
        # self.forward(5)
