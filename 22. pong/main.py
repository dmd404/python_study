from turtle import Screen
from paddle import Paddle

paddle = Paddle()


def main():
    screen = Screen()
    screen.title('My pong game')
    screen.bgcolor('black')
    screen.setup(width=800, height=600)
    screen.tracer(0)

# move paddle using keystrokes
    screen.listen()
    screen.onkey(paddle.up, 'Up')
    screen.onkey(paddle.down, 'Down')

    game_is_on = True
    while game_is_on:
        screen.update()

    screen.exitonclick()


if __name__ == '__main__':
    main()
