import random
from turtle import Turtle, Screen

screen = Screen()



def turtle_race():
    screen.clearscreen()
    screen.setup(width=500, height=400)
    screen.tracer(0)

    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    pos_y = -125
    turtles= []

    def random_dist():
        return random.randint(0, 20)

    for index in range(6):
        current_y = pos_y + (index * 50)
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[index])
        new_turtle.penup()
        new_turtle.goto(-220, current_y )
        turtles.append(new_turtle)
    screen.update()
    screen.tracer(1)
    user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a color: ")

    race_is_on = True
    winner = ""

    while race_is_on:
        for turtle in turtles:
            turtle.forward(random_dist())
            if turtle.xcor()  >= 220:
                winner = turtle.pencolor()
                race_is_on = False
                break

    if user_bet == winner:
        new_game= screen.textinput(title="You Won!", prompt="Play again? Answer Yes or No").lower()
    else:
        new_game = screen.textinput(title="You lost!", prompt="Play again? Answer Yes or No").lower()
    if new_game == "no":
        return False
    else:
        return True

play_again = True
while play_again:
    play_again = turtle_race()


screen.exitonclick()