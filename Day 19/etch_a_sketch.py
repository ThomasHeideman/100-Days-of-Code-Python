from tabnanny import format_witnesses
from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()

def move_forwards():
    pen.forward(10)

def move_backwards():
    pen.backward(10)

def rotate_counter_clockwise():
    new_heading = pen.heading() + 10
    pen.setheading(new_heading)
def rotate_clockwise():
    new_heading = pen.heading() - 10
    pen.setheading(new_heading)
def clear():
    pen.clear()
    pen.penup()
    pen.home()
    pen.pendown()

print(pen.position())
screen.listen()
screen.onkey(key="w",fun=move_forwards)
screen.onkey(key="s",fun=move_backwards)
screen.onkey(key="a",fun=rotate_counter_clockwise)
screen.onkey(key="d",fun=rotate_clockwise)
screen.onkey(key="c",fun=clear)

screen.exitonclick()