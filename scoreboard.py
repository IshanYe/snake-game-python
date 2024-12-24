from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.up()
        self.goto(0, 270)
        self.write(f"Score = {self.score}", align="center", font=("Courier", 20, "normal"))
        self.hideturtle()

    def increase(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", align="center", font=("Courier", 20, "normal"))

    def stop(self):
        self.goto(0, 0)
        self.write("Game Over.", align="center", font=("Courier", 20, "normal"))
