from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

x_pos = [0, -20, -40]

segments = []

for _ in x_pos:
    white_square = Turtle(shape='square')
    white_square.penup()
    white_square.color('white')
    white_square.setx(_)
    segments.append(white_square)


game_is_on = True
while game_is_on:
    for seg in segments:
        seg.forward(20)
        screen.update()

screen.exitonclick()