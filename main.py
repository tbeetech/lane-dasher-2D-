
import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
# create a player object and trigger screen to listen to key events
player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
# a new car deployer instance
car_deployer = CarManager()


while game_is_on:


    time.sleep(0.1)
    screen.update()
    car_deployer.create_cars()
    car_deployer.move_cars()

    for car in car_deployer.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over_trigger()
    if player.reached_finish_line():
        player.go_to_start()
        car_deployer.level_upgrade()
        scoreboard.increase_level()





screen.exitonclick()
