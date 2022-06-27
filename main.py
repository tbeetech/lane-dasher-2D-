import time
import turtle
from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

PLAYER = Player()
SCOREBOARD = Scoreboard()
CAR_DEPLOYER = CarManager()

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgpic('resources/lane.gif')
screen.listen()
screen.onkey(PLAYER.go_up, "Up")
screen.onkeypress(PLAYER.run, 'Up')


def switch_game_on():
    game_is_on = True
    return game_is_on


def all_reset():
    PLAYER.reset_player()
    SCOREBOARD.reset_scoreboard()
    CAR_DEPLOYER.reset_car()
    screen.update()
    run_game(switch_game_on)


def run_game(game_is_on):
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        CAR_DEPLOYER.create_cars()
        CAR_DEPLOYER.move_cars()
        for car in CAR_DEPLOYER.all_cars:
            if car.distance(PLAYER) < 20:
                game_is_on = False
                SCOREBOARD.game_over_trigger()

        if PLAYER.reached_finish_line():
            PLAYER.go_to_start()
            CAR_DEPLOYER.level_upgrade()
            SCOREBOARD.increase_level()




run_game(switch_game_on)

screen.onkey(all_reset, 'r')

if screen.exitonclick():
    turtle.clearscreen()
