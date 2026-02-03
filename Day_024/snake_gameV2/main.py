from turtle import Screen

from scoreboard import ScoreBoard
from snake import Snake
from food import Food
screen = Screen()
import time

def play_snake():
    screen.clearscreen()
    screen.setup(width=600, height=600)
    screen.title("My Snake Game")
    screen.bgcolor("DarkOliveGreen3")

    screen.tracer(0)
    snake = Snake()
    food = Food()
    scoreboard = ScoreBoard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.15)

        snake.move()
        # detect when snake catches food
        if snake.head.distance(food) < 15:
            food.spawn()
            scoreboard.increase_score()
            snake.extend()

        #Detect collision with wall
        if snake.head.xcor() > 280 or  snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.reset_game()
            snake.reset_snake()

        #Detect collision with tail
        for bit in  snake.snake_bits[1:]:
            if snake.head.distance(bit) < 10:
                scoreboard.reset_game()
                snake.reset_snake()

    new_game = screen.textinput(title="You lost!", prompt="Play again? Answer Yes or No").lower()
    if new_game == "no":
        return False
    else:
        return True

play_again = True
while play_again:
    play_again = play_snake()

screen.exitonclick()