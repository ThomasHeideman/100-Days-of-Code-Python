from symtable import Class
from turtle import Turtle, Screen
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_bits = []
        self.create_snake()
        self.head =self.snake_bits[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def move(self):
        for snake_bit_num in range(len(self.snake_bits) - 1, 0, -1):
            new_x = self.snake_bits[snake_bit_num - 1].xcor()
            new_y = self.snake_bits[snake_bit_num - 1].ycor()
            self.snake_bits[snake_bit_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        snake_bit = Turtle(shape="square")
        snake_bit.color("DarkSlateGrey")
        snake_bit.penup()
        snake_bit.goto(position)
        self.snake_bits.append(snake_bit)

    def extend(self):
        self.add_segment(self.snake_bits[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

