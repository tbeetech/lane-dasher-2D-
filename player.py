from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('white')
        self.penup()
        self.current_player_pos = self.pos()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)
        self.current_player_pos = self.pos()
        print(f'player is @ location:\n*{self.current_player_pos}*')

    def run(self):
        self.forward(MOVE_DISTANCE)
        self.current_player_pos = self.pos()
        print(f'player is @ location:\n*{self.current_player_pos}*')

    def reset_player(self):
        self.go_to_start()

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def reached_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            print('completion validation working')
            return True
        return False
