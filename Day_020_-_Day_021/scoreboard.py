from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 16, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score= 0
        self.color("DarkSlateGrey")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.show_score()

    def show_score(self):
        self.write(f"Score: {self.score}", False, align= ALIGNMENT, font= FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.show_score()

    def game_over(self):
        self.hideturtle()
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER!", False, align=ALIGNMENT, font=FONT)

