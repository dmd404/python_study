from turtle import Screen
import time

screen = Screen()


def main():
    screen.setup(600, 600)
    screen.tracer(0)

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)

    screen.exitonclick()

if __name__ == '__main__':
    main()
