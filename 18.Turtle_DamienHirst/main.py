from turtle import Turtle, Screen
import random

screen = Screen()
tim = Turtle()
tim.shape('turtle')  # change shape to turtle
tim.color('blue')  # change color

# # Challenge 1: draw a square
# for i in range(4):
#     tim.fd(100)
#     tim.rt(90)


# # Challenge 2: draw a dashed line
# for _ in range(10):
#     tim.fd(10)
#     tim.pu()
#     tim.fd(10)
#     tim.pd()
#
#
# def dashed_line(turtle, num_lines):
#     for _ in range(num_lines):
#         turtle.fd(10)
#         turtle.pu()
#         turtle.fd(10)
#         turtle.pd()
# # dashed_line(tim, 5)

# Challenge 3: Draw different shapes triangle to decagon
# each of the shape drawn with random color
# each sides with lengh of 100
def draw_shape(length, num_sides):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.color((r, g, b))
    for _ in range(num_sides):
        tim.fd(length)
        tim.rt(360/num_sides)


screen.colormode(255)
for _ in range(3, 11):
    draw_shape(100, _)

screen.exitonclick()  # window disappears when clicked on
