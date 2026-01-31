from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 16, 'bold')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_a= 0
        self.score_b= 0
        self.color("white")
        self.penup()
        self.hideturtle()

        self.show_score()
    def draw_background(self):
        self.goto(-60, 290)  # Ga naar de hoek van je vakje
        self.color("blue")  # De kleur van je achtergrond
        self.begin_fill()
        for _ in range(2):
            self.forward(120)  # Breedte van het vak
            self.right(90)
            self.forward(60)  # Hoogte van het vak
            self.right(90)
        self.end_fill()
        self.color("white")  # Zet kleur terug voor de tekst

    def show_score(self):
        self.clear()
        self.draw_background()
        self.goto(0, 260)
        self.write("SCORE", align=ALIGNMENT, font=FONT)

        self.goto(0, 235)
        self.write(f"{self.score_a}   -   {self.score_b}", align=ALIGNMENT, font=FONT)

    def update_score(self, side):
        if side == 'a':
            self.score_a += 1
        if side == 'b':
            self.score_b += 1
        self.clear()
        self.show_score()


