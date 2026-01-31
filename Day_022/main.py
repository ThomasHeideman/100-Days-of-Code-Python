from turtle import Screen

from scoreboard import ScoreBoard
from dashed_line import Dashed_line
from paddle import Paddle
from ball import Ball

import time
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)
screen.listen()
dashed_line = Dashed_line()
left_paddle = Paddle((-350,0))
right_paddle= Paddle((350,0))
ball = Ball()
scoreboard = ScoreBoard()

screen.onkeypress(right_paddle.up, key="Up")
screen.onkeypress(right_paddle.down, key="Down")
screen.onkeypress(left_paddle.up, key="w")
screen.onkeypress(left_paddle.down, key="s")


def play_set():

    time.sleep(0.05)
    ball.move_ball()
    screen.update()
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()
    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_paddle()

    if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()

    # detect if ball is missed
    if ball.xcor() > 360:
        ball.reset_ball()
        scoreboard.update_score("a")
    if ball.xcor() < -360:
        ball.reset_ball()

        scoreboard.update_score("b")


game_on = True
while game_on:
    play_set()



screen.update()
screen.exitonclick()

