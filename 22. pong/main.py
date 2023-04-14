from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title('My pong game')
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

def main():
# move paddle using keystrokes
    screen.listen()
    screen.onkey(r_paddle.up, 'Up')
    screen.onkey(r_paddle.down, 'Down')
    screen.onkey(l_paddle.up, 'w')
    screen.onkey(l_paddle.down, 's')

    game_is_on = True

    while game_is_on:
        time.sleep(ball.pace)  # sleep while loop between updates
        screen.update()
        ball.move()

        # Detect collision with wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            # needs to bounce
            ball.bounce_y()

        # Detect collision with paddle
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()

        # Detect when r_paddle misses
        if ball.xcor() > 400:
            ball.reset()
            scoreboard.l_point()
        # Detect when l_paddle misses
        if ball.xcor() < -400:
            ball.reset()
            scoreboard.r_point()


    screen.exitonclick()


if __name__ == '__main__':
    main()
