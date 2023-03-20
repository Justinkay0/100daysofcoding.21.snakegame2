from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(x=0, y=280)
        self.color('white')
        self.hideturtle()
        self.write(arg=f"Score = {self.score}", move= False, align='center', font=('Calibri', 12, 'normal'))

    def scoreboard_add(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score = {self.score}", move=False, align='center', font=('Calibri', 12, 'normal'))