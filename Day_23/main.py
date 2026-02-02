import time
from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()

def play_game():
    screen.clearscreen()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    player = Player()
    screen.listen()
    cars = CarManager()
    score = Scoreboard()
    screen.onkey(player.go_forward, "Up")
    screen.onkey(player.go_left, "Left")
    screen.onkey(player.go_right, "Right")

    game_is_on = True
    while game_is_on:

        time.sleep(0.1)
        cars.car()
        cars.move_cars()
        # detect player reached finishline
        if player.ycor() > 280:
            score.update_score()
            cars.level_up()
            player.reset_player()

        # detect collision
        for car in cars.cars:
            if car.distance(player) < 30:
                score.game_over()
                game_is_on = False
                break

        screen.update()

    new_game = screen.textinput(title="You lost!", prompt="Play again? Answer Yes or No").lower()
    if new_game == "no":
        return False
    else:
        return True

play_again = True
while play_again:
    play_again = play_game()



screen.exitonclick()
