from turtle import Turtle

MOVE_DISTANCE = 20
X_POSITIONS = [0, -20, -40]  # constants


class Snake:
    def __init__(self):
        self.segmets = []
        self.create_snake()

    def create_snake(self):
        for _ in X_POSITIONS:
            white_square = Turtle(shape='square')
            white_square.penup()
            white_square.color('white')
            white_square.setx(_)
            self.segments.append(white_square)

    def move(self):
    # move snake forward by 20 pixels
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        segments[0].forward(MOVE_DISTANCE)