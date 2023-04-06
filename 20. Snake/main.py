from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")

x_pos = [0, -20, -40]

for _ in x_pos:
    white_square = Turtle(shape='square')
    white_square.penup()
    white_square.color('white')
    white_square.setx(_)

screen.exitonclick()