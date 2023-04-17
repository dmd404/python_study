from turtle import Screen
import random
import time
from player import Player
from car_manager import CarManager

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
screen = Screen()
all_cars = []

def main():
    screen.setup(600, 600)
    screen.tracer(0)

    player = Player()
    car_manager = CarManager()

    screen.listen()
    screen.onkey(player.up, 'Up')


    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        car_manager.create_car()
        car_manager.move_cars()

        # car.move()
        # for car in all_cars:
        #     car.forward(2)

    # Detect collision with top wall
        if player.ycor() > 280:
            player.goto(0, -270)

    screen.exitonclick()

if __name__ == '__main__':
    main()
