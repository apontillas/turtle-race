from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def winner(self):
        self.write(f"You Won!", False, align="center", font=('Courier', 30, 'normal'))

    def loser(self):
        self.write(f"You Lose!", False, align="center", font=('Courier', 30, 'normal'))
