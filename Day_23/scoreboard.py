from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT= "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.show_score()

    def show_score(self):
        self.write(f"level {self.score}",move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.show_score()

    def game_over(self):
        self.hideturtle()
        self.clear()
        self.color("black")
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)