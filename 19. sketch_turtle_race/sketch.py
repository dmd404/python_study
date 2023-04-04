from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def tilt_clock():
    tim.right(10)


def tilt_anticlock():
    tim.left(10)


def clear_drawing():
    screen.resetscreen()


"""
W = forward
s = backwards
a = counter-clockwise
d = clockwise
c = clear drawing
"""
screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=tilt_anticlock)
screen.onkey(key='d', fun=tilt_clock)
screen.onkey(key='c', fun=clear_drawing)
screen.exitonclick()
