from turtle import Turtle

FONT = ("input mono", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color('green')
        self.goto(-280, 250)
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f'level: {self.level}', align='left', font=FONT, )

    def increase_level(self):
        self.level += 1
        self.update_score_board()

    def game_over_trigger(self):

        self.clear()
        self.color('red')
        self.write(f'You lost click "R" to restart', align='left', font=FONT)
        self.color('green')

    def reset_scoreboard(self):
        self.clear()
        self.write(f'level: {1}', align='left', font=FONT, )
