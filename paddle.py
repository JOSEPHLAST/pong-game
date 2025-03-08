from turtle import Turtle

PADDLE_POSITIONS = [(-380, 0), (370, 0)]
MOVE = 20

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.paddles = []
        self.blit_paddle()
        self.l_paddle = self.paddles[0]
        self.r_paddle = self.paddles[1]

    def blit_paddle(self):
        for pos in PADDLE_POSITIONS:
            paddle = Turtle("square")
            paddle.color("white")
            paddle.speed(0)
            paddle.shapesize(5, 1)
            paddle.penup()
            paddle.goto(pos)
            self.paddles.append(paddle)

    def l_paddle_up(self):
        y_pos = self.l_paddle.ycor() + MOVE
        if y_pos <= 200:
            self.l_paddle.sety(y_pos)

    def l_paddle_down(self):
        y_pos = self.l_paddle.ycor() - MOVE
        if y_pos >= -200:
            self.l_paddle.sety(y_pos)

    def r_paddle_up(self):
        y_pos = self.r_paddle.ycor() + MOVE
        if y_pos <= 200:
            self.r_paddle.sety(y_pos)

    def r_paddle_down(self):
        y_pos = self.r_paddle.ycor() - MOVE
        if y_pos >= -200:
            self.r_paddle.sety(y_pos)