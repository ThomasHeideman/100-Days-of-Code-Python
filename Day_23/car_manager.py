from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
LANES = [-220, -180, -140, -100, -60, -20, 20, 60, 100, 140, 180, 220]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5



class CarManager:
    def __init__(self):
        self.cars = []
        self.car_freq = 8
        self.movement = STARTING_MOVE_DISTANCE
        self.car()


    def car(self):
        randomizer = random.randint(1, self.car_freq)
        if randomizer == self.car_freq:
            rand_y = random.choice(LANES)
            color = random.choice(COLORS)
            car =  Turtle(shape="square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.setheading(180)
            car.color(color)
            car.goto(300,rand_y)
            self.cars.append(car)




    def move_cars(self):
        for car in self.cars:
            car.forward(self.movement)
            if car.xcor() < -320:
                car.hideturtle()
        self.cars = [car for car in self.cars if car.xcor() > -320]



    def level_up(self):
        self.movement += MOVE_INCREMENT
        self.car_freq -= 2
        if self.car_freq < 2: self.car_freq = 2

