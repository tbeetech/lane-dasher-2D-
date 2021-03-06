# Rename to car deployer
import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.goto(300, random.randint(-250, 250))

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            # car design
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            # deploy car at random position on Y axis
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_upgrade(self):
        self.car_speed += MOVE_INCREMENT

    def reset_car(self):
        for each_car in self.all_cars:
            each_car.clear()
        self.car_speed = STARTING_MOVE_DISTANCE
