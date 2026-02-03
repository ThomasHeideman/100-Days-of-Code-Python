from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 16, 'normal')


def read_highscore():
    try:
        with open("data.txt", mode="r") as file:
            return int(file.read())
    except FileNotFoundError:
        with open("data.txt", mode="w") as file:
            file.write("0")
        return 0

def write_highscore(score):
    with open("data.txt", mode="w") as file:
        file.write(score)

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score= 0
        self.high_score = read_highscore()
        self.color("DarkSlateGrey")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align= ALIGNMENT, font= FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_game(self):
        if self.score > self.high_score:
            write_highscore(str(self.score))
        self.high_score = read_highscore()
        self.score = 0
        self.update_scoreboard()
