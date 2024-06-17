from turtle import Turtle
ALIGN = "center"
FONT = ("ACourier", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score} ", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()

    def update_score(self):
        self.write(f"Score: {self.score} ", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} ", align="center", font=("Arial", 24, "normal"))

