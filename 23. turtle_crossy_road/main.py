from turtle import Screen
import time
from player import Player

screen = Screen()


def main():
    screen.setup(600, 600)
    screen.tracer(0)

    player = Player()

    screen.listen()
    screen.onkey(player.up, 'Up')


    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)

    # Detect collision with top wall
        if player.ycor() > 260:
            player.goto(0, -270)

    screen.exitonclick()

if __name__ == '__main__':
    main()
