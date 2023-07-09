from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as file:
            self.high_in_data = int(file.read())
        self.color("White")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.high_score()
        self.write(f"Score : {self.score}  HighScore: {self.high_in_data}", move=False, align="center",
                   font=("Arial", 12, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(0, 80)
        self.color("Red")
        self.write("GAME OVER!", align="center", font=("Nonito", 20, "bold"))
        self.goto(0, 30)
        self.color("White")
        self.write(f"YOUR SCORE : {self.score}", align="center", font=("Courier", 25, "bold"))
        self.goto(0, -10)
        self.color("Green")
        self.write(f"HIGH SCORE : {self.high_in_data}", align="center", font=("Times New Roman", 20, "bold"))

    def high_score(self):
        if self.score > self.high_in_data:
            with open("highscore.txt", mode='w') as file:
                file.write(f"{self.score}")
