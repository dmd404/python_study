from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
scoreboard = Scoreboard()

def main():
    screen.setup(600, 600)
    screen.tracer(0)
    screen.title('Turtle Crossy Road')

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

    # Detect collision with top wall
        if player.is_at_finish_line():
            player.go_to_start()
            scoreboard.next_level()
            car_manager.speed_up()

    # Detect collision with car
        for car in car_manager.all_cars:
            if player.distance(car) < 20:
                game_is_on = False
                scoreboard.game_over()

    screen.exitonclick()

if __name__ == '__main__':
    main()
