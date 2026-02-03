from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 12, 'normal')

class Name(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

    def print(self,state,location):
        self.goto(location)
        self.write(f"{state}", False, align=ALIGNMENT, font=FONT)

