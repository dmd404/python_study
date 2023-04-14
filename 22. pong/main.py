from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.title('My pong game')
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

def main():
# move paddle using keystrokes
    screen.listen()
    screen.onkey(r_paddle.up, 'Up')
    screen.onkey(r_paddle.down, 'Down')
    screen.onkey(l_paddle.up, 'w')
    screen.onkey(l_paddle.down, 's')

    game_is_on = True


    while game_is_on:
        time.sleep(0.1)  # sleep while loop between updates
        screen.update()
        ball.move('test')

        # Detect collision with wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            # needs to bounce
            ball.bounce()

    screen.exitonclick()


if __name__ == '__main__':
    main()
