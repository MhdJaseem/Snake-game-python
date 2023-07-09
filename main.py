from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


def game_start():
    # UI Setup
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("Black")
    screen.title("My Snake Game")
    screen.tracer(0)
    screen.listen()

    cobra = Snake()
    food = Food()
    score = ScoreBoard()

    # Button Command
    screen.onkey(cobra.up, "Up")
    screen.onkey(cobra.down, "Down")
    screen.onkey(cobra.right, "Right")
    screen.onkey(cobra.left, "Left")

    def restart():
        choice = screen.textinput("GAME OVER", "Do you wanna play again? Hit Enter")
        if choice == '':
            return True
        else:
            return False

    game_is_on = True
    move = True
    while game_is_on:
        while move:
            # Snake Movement
            time.sleep(0.1)
            cobra.move_snake()
            screen.update()

            # Food Collision
            if cobra.head.distance(food) < 15:
                food.refresh()
                for part in cobra.snake:
                    if food.distance(part) < 15:
                        food.refresh()
                score.increase_score()
                screen.update()
                cobra.grow()

            # Wall Collision
            if cobra.head.xcor() > 280 or cobra.head.xcor() < -280 or cobra.head.ycor() > 280 or cobra.head.ycor() < -\
                    280:
                score.game_over()
                move = False
                if restart():
                    screen.resetscreen()
                    game_start()
                else:
                    screen.bye()
                    return

            # Snake body Collision
            for part in cobra.snake[1:]:
                if cobra.head.distance(part) < 15:
                    score.game_over()
                    move = False
                    if restart():
                        screen.resetscreen()
                        game_start()
                    else:
                        screen.bye()
                        return


game_start()
