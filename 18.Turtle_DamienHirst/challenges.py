from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)
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

# # Challenge 3: Draw different shapes triangle to decagon
# # each of the shape drawn with random color
# # each sides with lengh of 100
# def draw_shape(length, num_sides):
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     tim.color((r, g, b))
#     for _ in range(num_sides):
#         tim.fd(length)
#         tim.rt(360/num_sides)
#
#
# for _ in range(3, 11):
#     draw_shape(100, _)

# Challenge 4: Random walk
# thicker, and faster
# direction = [0, 90, 180, 270]
# # tim.speed(10)
# tim.pensize(10)
# tim.speed(0)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
#
# for _ in range(20):
#     tim.color(random_color())
#     tim.fd(30)
#     tim.setheading(random.choice(direction))
# # def random_walk():
# #     tim.pensize(10)
# #
# #     for _ in range(90):
# #         tim.speed(10)
# #         r = random.randint(0, 255)
# #         g = random.randint(0, 255)
# #         b = random.randint(0, 255)
# #         tim.color(r, g, b)
# #         direction = random.randint(0, 1)
# #         head = random.randint(0, 1)
# #         if direction == 0:
# #             tim.lt(90)
# #         else:
# #             tim.rt(90)
# #         if head == 0:
# #             tim.fd(50)
# #         else:
# #             tim.bk(50)
# #
# #
# # random_walk()



# Challenge 5: Spirograph with radius size of 100
# count = 0
# for _ in range(50):
#     count += 10
#     tim.color(random_color())
#     tim.speed('fastest')
#     tim.circle(100)
#     tim.setheading(count)

tim.speed('fastest')
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)
screen.exitonclick()  # window disappears when clicked on
