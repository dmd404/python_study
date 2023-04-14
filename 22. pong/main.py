from turtle import Screen
from paddle import Paddle

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

def main():
    screen = Screen()
    screen.title('My pong game')
    screen.bgcolor('black')
    screen.setup(width=800, height=600)
    screen.tracer(0)

# move paddle using keystrokes
    screen.listen()
    screen.onkey(r_paddle.up, 'Up')
    screen.onkey(r_paddle.down, 'Down')
    screen.onkey(l_paddle.up, 'w')
    screen.onkey(l_paddle.down, 's')

    game_is_on = True
    while game_is_on:
        screen.update()

    screen.exitonclick()


if __name__ == '__main__':
    main()
