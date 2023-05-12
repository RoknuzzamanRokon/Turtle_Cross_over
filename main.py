import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.up_key, 'w')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # Detect collision with car.
    for car in car_manager.all_car:
        if car.distance(player) < 20:
            scoreboard.game_over_massage()
            game_is_on = False

    # Detect successful crossing.
    if player.move_finish_line():
        player.goto_start_position()
        car_manager.lvl_up_car_speed()
        scoreboard.increase_scoreboard()

screen.exitonclick()
