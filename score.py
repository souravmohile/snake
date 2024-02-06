from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as high_score:
            self.high_score = int(high_score.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as high_score:
                high_score.write(f"{self.high_score}")

        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align="center", font=("Arial", 24, "normal"))
