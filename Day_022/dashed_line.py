from turtle import  Turtle


class Dashed_line():
    
    def __init__(self):
        self.dashed_line = Turtle()
        self.dashed_line.hideturtle()
        self.dashed_line.penup()
        self.dashed_line.color("white")
        self.dashed_line.pensize(1)
        self.dashed_line.goto(0, -300)
        self.dashed_line.pendown()
        self.dashed_line.setheading(90)
        for _ in range(30):
            self.dashed_line.forward(15)
            self.dashed_line.penup()
            self.dashed_line.forward(15)
            self.dashed_line.pendown()
