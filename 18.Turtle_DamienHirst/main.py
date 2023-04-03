from turtle import Turtle, Screen
import random
import colorgram

raw_colors = []
colors = colorgram.extract('image.jpeg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    raw_colors.append(new_color)

color_list = raw_colors[3:]
screen = Screen()
tim = Turtle()
screen.colormode(255)
tim.penup()

# def paint(x, y):
#     tim.setx(x)
#     tim.sety(y)
#     for _ in range(10):
#         tim.dot(20, random.choice(color_list))
#         tim.penup()
#         tim.fd(50)
#
#
# startx = -250
# starty = -200
# for _ in range(10):
#     paint(startx, starty)
#     starty += 50

tim.setheading(225)
tim.fd(300)
tim.setheading(0)
number_of_dots = 100
tim.speed(0)
tim.penup()
tim.hideturtle()
for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(180)
        tim.fd(500)
        tim.setheading(0)

screen.exitonclick()

